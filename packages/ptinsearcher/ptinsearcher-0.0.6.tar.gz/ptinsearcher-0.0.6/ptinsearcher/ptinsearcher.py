#!/usr/bin/python3
"""
    ptinsearcher - Web sources information extractor

    Copyright (c) 2020 HACKER Consulting s.r.o.

    ptinsearcher is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ptinsearcher is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ptinsearcher.  If not, see <https://www.gnu.org/licenses/>.
"""

__version__ = "0.0.6"

import argparse
import copy
import html
import os
import re
import stat
import sys
import tempfile
import urllib

from ptlibs import ptmisclib, ptjsonlib
from bs4 import BeautifulSoup

import exiftool
import tldextract
import requests


class ptinsearcher:
    def __init__(self, args):
        self.use_json               = args.json
        self.ptjsonlib              = ptjsonlib.ptjsonlib(self.use_json)
        self.json_no                = self.ptjsonlib.add_json("ptinsearcher")
        self.headers                = ptmisclib.get_request_headers(args)
        self.proxies                = {"http": args.proxy, "https": args.proxy}
        self.timeout                = 15
        self.post_data              = args.post_data
        self.method                 = "GET" if not args.post_data else "POST"
        self.redirects              = args.redirects
        self.domain                 = self._get_domain(args.domain)
        self.url_list               = list(dict.fromkeys(self._get_url_list(args)))
        self.grouping               = args.grouping
        self.grouping_complete      = args.grouping_complete
        self.group_parameters       = args.group_parameters
        self.without_parameters     = args.without_parameters
        self.output_file            = args.output
        self.output_parts           = args.output_parts
        self.script_home_folder     = os.path.join(os.path.expanduser('~'), SCRIPTNAME)
        self.file_handler           = None
        self.grouping_group         = None

        self.extract_types = self.get_extract_types(args.extract)
        self.ptjsonlib.add_data(self.json_no, {"urls": []})

        if args.output and not os.path.exists(self.script_home_folder):
            os.makedirs(self.script_home_folder)
        if args.grouping and args.grouping_complete:
            ptmisclib.end_error("Cannot use both -g and -gc parameters together", self.json_no, self.ptjsonlib, self.use_json)
        if args.output_parts and not args.output:
            ptmisclib.end_error("Missing --output parameter", self.json_no, self.ptjsonlib, self.use_json)
        if args.output and not args.output_parts:
            self.file_handler = open(os.path.join(self.script_home_folder, self.output_file), "w")

    def run(self, args):
        self._iterate_websites(args)

        if self.grouping or self.grouping_complete and not self.use_json:
            self.print_result(self.ptjsonlib.json_list[0]["data"]["urls"]) # send full json

        if self.file_handler:
            ptmisclib.ptprint(ptmisclib.out_ifnot(f"Output saved to {self.script_home_folder}/{args.output}", "INFO", self.use_json))
            self.file_handler.close()

        ptmisclib.ptprint(ptmisclib.out_if(self.ptjsonlib.get_all_json(), "", self.use_json), end="")

    def _iterate_websites(self, args):
        for index, url in enumerate(self.url_list):
            self.data = {"url": "null", "status": "null", "vulnerable": "null", "content-type": "null", "data": []}
            self.url = url
            self.result_data = {}
            self.is_file = None
            current_iteration_position_str = f'[{index+1}/{len(self.url_list)}]' if len(self.url_list) > 1 else ""
            ptmisclib.ptprint(ptmisclib.out_ifnot(f" ", "", self.use_json))
            ptmisclib.ptprint(ptmisclib.out_title_ifnot(f"Testing: {url} {current_iteration_position_str}", self.use_json))

             # If source is a file
            if os.path.exists(self.url):
                if self.grouping_group == "sites_only":
                    ptmisclib.ptprint(ptmisclib.out_ifnot(f"Testing files not possible when group testing sites", "ERROR", self.use_json))
                    continue
                path2file = os.path.abspath(self.url)
                self.is_file = True
                ptmisclib.ptprint(ptmisclib.out_ifnot(f"Response: is-file", "INFO", self.use_json))
                self.data.update({"url": path2file, "is_file": self.is_file})
                if (self.grouping or self.grouping_complete) and not self.grouping_group:
                    self.grouping_group = "files_only"
                self.process_file(path2file)

            # If source is a website
            else:
                if self.grouping_group == "files_only":
                    ptmisclib.ptprint(ptmisclib.out_ifnot(f"Testing sites not possible when group testing files", "ERROR", self.use_json))
                    continue
                try:
                    response = requests.request(self.method, url, allow_redirects=self.redirects, timeout=self.timeout, headers=self.headers, proxies=self.proxies, verify=False, data=self.post_data)
                    response.encoding = response.apparent_encoding
                except Exception as e:
                    ptmisclib.ptprint(ptmisclib.out_ifnot(f"Server not responding", "ERROR", self.use_json))
                    self.data.update({"status": "error", "message": str(e)})
                    continue

                ptmisclib.ptprint(ptmisclib.out_ifnot(f"Response: {response.url} [{response.status_code}]", "INFO", self.use_json), end=" ")
                if str(response.status_code).startswith("3"):
                    if response.headers.get("location"):
                        ptmisclib.ptprint(ptmisclib.out_ifnot(f"-> {ptmisclib.get_colored_text(response.headers['location'], 'INFO')}", "", self.use_json))
                    if not self.redirects:
                        if not response.headers.get("location"):
                            ptmisclib.ptprint(ptmisclib.out_ifnot(" ", '', "", self.use_json))
                        error_msg = "Redirects disabled, not following"
                        ptmisclib.ptprint(ptmisclib.out_ifnot(error_msg, "ERROR", self.use_json))
                        self.data.update({"url": response.url, "status": "error", "message": error_msg})
                        self.ptjsonlib.add_data(self.json_no, self.data)
                        continue

                ptmisclib.ptprint(ptmisclib.out_ifnot(" ", "", self.use_json))
                if (self.grouping or self.grouping_complete) and not self.grouping_group:
                    self.grouping_group = "sites_only"
                self.process_response(response)

    def process_response(self, response):
        TEXT_CONTENT = ["text/html", "text/plain", "text/css", "text/cvs", "text/javascript", "application/json", "application/xml"]
        XML_CONTENT = ["application/xml", "text/xml"]
        content_type = response.headers.get("content-type").split(";")[0]
        ptmisclib.ptprint(ptmisclib.out_ifnot(f"Content-Type: {content_type}", "INFO", self.use_json))
        self.data.update({"url": response.url, "status": "ok", "content-type": content_type})
        self.scrape_website(response)

    def process_file(self, file_location):
        """read file, if exc, get only metadata"""
        re_possible_links = r"(((http|ftp|https|irc)://)|(www\.))([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
        re_email = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,3}'
        re_ip = r'(?<![\.\+\-])\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
        file_type = file_location.split("/")[-1].split(".")[-1]
        found_links = None
        metadata = None
        is_readable = None
        emails = None
        ptmisclib.ptprint(ptmisclib.out_ifnot(f"File-type: {file_type}", "INFO", self.use_json))
        try:
            with open(self.url, 'r') as fh:
                file_content = fh.read()
            is_readable = True
        except Exception as e:
            e = "Could not read file contents"
            ptmisclib.ptprint(ptmisclib.out_ifnot(e, "ERROR", self.use_json))
            emails = [e]
            found_links = [e]
            is_readable = False
        if is_readable:
            if self.extract_types["emails"]:
                emails = self._find(file_content, re_email)
            if self.extract_types["internal_urls"] or self.extract_types["external_urls"] or self.extract_types["internal_urls_with_parameters"] or self.extract_types["subdomains"]:
                found_links = self._find(file_content, re_possible_links)
                found_links = sorted(list(set(found_links)), key=str.lower)
            if self.extract_types["ip_addresses"]:
                found_ip_addresses = self._find(file_content, re_ip)
        if self.extract_types["metadata"]:
            metadata = self.get_metadata(path2file=file_location)
        self.result_data.update({"found_infile_links": found_links, "metadata": metadata, "emails": emails, "ip_addresses": found_ip_addresses})
        self.data["data"].append(self.result_data)
        self.ptjsonlib.json_list[0]["data"]["urls"].append(self.data)
        if not self.use_json and not (self.grouping or self.grouping_complete):
            self.print_result([self.ptjsonlib.json_list[0]["data"]["urls"][-1]])

    def parse_robots_txt(self, response):
        allow = list({pattern.lstrip() for pattern in re.findall(r"^Allow: ([\S ]*)", response.text, re.MULTILINE)})
        disallow = list({pattern.lstrip() for pattern in re.findall(r"^Disallow: ([\S ]*)", response.text, re.MULTILINE)})
        sitemaps = re.findall(r"[Ss]itemap: ([\S ]*)", response.text, re.MULTILINE)
        test_data = {"allow": allow, "disallow": disallow, "sitemaps": sitemaps}

        parsed_url = urllib.parse.urlparse(self.url)
        internal_urls = []
        for section_header in test_data.values():
            for finding in section_header:
                parsed_finding = urllib.parse.urlparse(finding)
                if not parsed_finding.netloc:
                    full_path = urllib.parse.urlunparse((parsed_url[0], parsed_url[1], parsed_finding[2], "", "", ""))
                else:
                    full_path = finding
                internal_urls.append(full_path)
        return internal_urls

    def scrape_website(self, response):
        """Extracts information from HTML page"""
        re_comment      = {"html": [r"<!--[\s\w\W]*?-->"], "css": [r"\/\*[^*]*\*+([^/*][^*]*\*+)*\/"], "js": ['\/\*[\s\S]+?\*\/']}
        re_email        = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,3}'
        re_ip           = r'(?<![\.\+\-])\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
        re_phone        = r"(?<![\w\/=\:-])(\(?\+\d{3}\)?[ -]?)?(\d{3}[ -]?)(\d{2,3}[ -]?)(\d{3}|\d{2} \d{2})(?![\w\"\'\/\\.])"
        re_abs_url      = r'(https?|ftps?)(://[\w\.]*\.[a-zA-Z]{2,3}[?&/#]*[^"\'><\s]*)'
        re_relative_url = r'(href=|src=)[\'"](.+?)[\'"]'

        comments                              =      None
        phone_numbers                         =      None
        emails                                =      None
        ip_addresses                          =      None
        abs_urls                              =      None
        forms                                 =      None
        subdomains                            =      None
        internal_urls                         =      None
        external_urls                         =      None
        metadata                              =      None
        metadata_tags                         =      None
        parsed_internal_urls_with_parameters  =      None

        soup = self.get_soup(response)
        page_content = urllib.parse.unquote(urllib.parse.unquote(html.unescape(soup.prettify())))

        if self.extract_types["html_comments"]:
            comments = list()
            for re_type in re_comment.keys():
                for comment_regex in re_comment[re_type]:
                    comments.extend(self._find(page_content, comment_regex))

        if self.extract_types["phone_numbers"]:
            phone_numbers = sorted(self._find(page_content, re_phone))
            phone_numbers = self.filter_phones(phone_numbers) # FIXME
        if self.extract_types["emails"]:
            emails = self._find(page_content, re_email)
        if self.extract_types["ip_addresses"]:
            ip_addresses = (self._find(page_content, re_ip))
        if self.extract_types["metadata"]:
            metadata = self.get_metadata(response.content)
        if self.extract_types["tags"]:
            metadata_tags = self.get_metadata_tags(soup)
        if self.extract_types["forms"]:
            forms = self.get_forms(soup)
        if self.extract_types["internal_urls"] or self.extract_types["external_urls"] or self.extract_types["internal_urls_with_parameters"] or self.extract_types["subdomains"]:
            abs_urls = self._find(page_content, re_abs_url)

            if response.url.endswith("robots.txt"):
                robots_data = self.parse_robots_txt(response)
                for data in robots_data:
                    if data not in abs_urls:
                        abs_urls.append(data)

        if self.extract_types["internal_urls"] or self.extract_types["internal_urls_with_parameters"]:
            internal_urls = self.find_urls(page_content, re_relative_url, response.url, "internal", abs_urls)
        if self.extract_types["internal_urls_with_parameters"]:
            parsed_internal_urls_with_parameters = self._sort(self.find_internal_parameters(internal_urls))
        if self.extract_types["external_urls"]:
            external_urls = self.find_urls(page_content, re_relative_url, response.url, "external", abs_urls)
        if self.extract_types["subdomains"]:
            subdomains = self.find_urls(page_content, re_relative_url, response.url, "subdomain", abs_urls)

        if internal_urls and not self.extract_types["internal_urls"]:
            internal_urls = None

        self.result_data.update({
            "html_comments": comments,
            "emails": emails,
            "phone_numbers": phone_numbers,
            "ip_addresses": ip_addresses,
            "internal_urls": internal_urls,
            "internal_urls_with_parameters": parsed_internal_urls_with_parameters,
            "external_urls": external_urls,
            "subdomains": subdomains,
            "forms": forms,
            "metadata": metadata,
            "metadata_tags": metadata_tags,
            })

        self.data["data"].append(self.result_data)
        self.ptjsonlib.json_list[0]["data"]["urls"].append(self.data)
        if not self.use_json and not (self.grouping or self.grouping_complete):
            self.print_result([self.ptjsonlib.json_list[0]["data"]["urls"][-1]])


    def get_metadata_tags(self, soup):
        """return author, robots, generator metadata"""
        author = soup.findAll("meta", {"name": "author"})
        robots = soup.findAll("meta", {"name": "robots"})
        generator = soup.findAll("meta", {"name": "generator"})
        result = {"author": [], "robots": [], "generator": []}
        for i in author:
            result["author"] += [i.attrs["content"]]
        for i in robots:
            result["robots"] += [i.attrs["content"]]
        for i in generator:
            result["generator"] += [i.attrs["content"]]
        return result

    def get_metadata(self, response_content=None, path2file=None):
        """return metadata"""
        executable = os.path.join(os.path.dirname(os.path.realpath(__file__)), "utils", "ExifTool", "exiftool")
        is_executable = os.access(executable, os.X_OK)
        blacklist = ["SourceFile", "ExifTool:ExifToolVersion", "File:FileName", "File:Directory", "File:Newlines"]
        metadata = dict()
        if not is_executable:
            try:
                os.chmod(executable, os.stat(executable).st_mode | stat.S_IEXEC)
            except:
                ptmisclib.end_error(f"Cannot execute nor set execution privileges for exiftool. Run script as sudo or try running 'sudo chmod +x {executable}'", self.json_no, self.ptjsonlib, self.use_json)
        if response_content:
            with tempfile.NamedTemporaryFile(mode="w+b", suffix="") as tmpfile:
                tmpfile.write(response_content)
                tmpfile.flush()
                with exiftool.ExifTool(executable_=executable) as et:
                    metadata = et.get_metadata(tmpfile.name)
                    blacklist = ["SourceFile", "ExifTool:ExifToolVersion", "File:Directory"]
        if path2file:
            with exiftool.ExifTool(executable_=executable) as et:
                metadata = et.get_metadata(path2file)
        if metadata.get('File:FileName'):
            metadata['File:FileName'] = self.url
        for i in blacklist:
            if metadata.get(i):
                metadata.pop(i)
        return metadata

    def find_urls(self, page_content, re_pattern, url, type_urls, result_old=[]):
        rslt = []
        domain = self.url2domain(url)
        all_urls = list({result[1] for result in re.findall(re_pattern, page_content)}) + result_old
        for found_url in all_urls:
            if found_url.startswith("mailto:") or found_url.startswith("javascript:"):
                continue
            if found_url.startswith("//"):
                o = urllib.parse.urlparse(self.url)
                all_urls.append(o.scheme + ":" + found_url)
                continue
            abs_url = self.rel2abs(found_url, domain)
            o = urllib.parse.urlparse(abs_url)
            if self.without_parameters:
                abs_url = urllib.parse.urlunsplit((o[0], o[1], o[2], "", ""))
            if type_urls == "external" and (self.url2domain(abs_url, False, False) != self.url2domain(url, False, False)):
                rslt.append(abs_url)
            if (type_urls == "subdomain") and (self.url2domain(abs_url, False, False) == self.url2domain(url, False, False)):
                rslt.append(o.netloc)
                rslt.append(o.netloc)
            if type_urls == "internal" and (self.url2domain(abs_url, True, False) == self.url2domain(url, True, False)):
                rslt.append(abs_url)
        return sorted(list(set(rslt)), key=str.lower)

    def filter_phones(self, phone_list):
        result = []
        for n in phone_list:
            tmp = ''.join(n.split())
            tmp = tmp.replace("-", "")
            if tmp.startswith("+"):
                req_len = len(tmp[1:])
            else:
                req_len = len(tmp)
            if req_len in [9, 12]:
                if n not in result:
                    result.append(n)
        return result

    def _sort(self, url_list):
        return sorted(url_list, key=lambda k: k['url'])

    def url2domain(self, url, with_subdomains=True, with_protocol=True):
        """Returns domain from supplied url"""
        tsd, td, tsu = tldextract.extract(url)
        if tsd:
            tsd = tsd + "."
        if with_protocol:
            protocol = url.split("//")[0]
        else:
            protocol = ""
        if with_subdomains:
            if not tsu:
                return protocol + "//" + tsd + td
            return protocol + "//" + tsd + td + "." + tsu
        else:
            if not tsu:
                return protocol + "//" + td + "." + tsu
            return protocol + "//" + td + "." + tsu

    def print_result(self, dict_list):
        if self.output_parts:
            parsed_file_name = self.output_file.rsplit(".", 1)
            file_extension = "." + parsed_file_name[-1] if len(parsed_file_name) > 1 else ""

        # Get headers
        first_dictionary = dict_list[0]
        first_dictionary["data"][0] = {k: v for k, v in first_dictionary["data"][0].items() if v is not None} # removes not included-in-test headers (testtypes)
        section_headers = [i for i in first_dictionary["data"][0].keys()]

        metadata_printed= False

        # Iterate headers
        for section_header in section_headers:
            separator = "\n"

            if self.output_parts:
                self.file_handler = open(os.path.join(self.script_home_folder, f"{parsed_file_name[0]}({section_header[0].upper()}){file_extension}"), "w")

            if self.grouping_complete:
                if section_header == "forms":
                    grouping_result = list()
                else:
                    grouping_result = set()

            # Print header
            ptmisclib.ptprint(ptmisclib.out_ifnot(f'\n{ptmisclib.get_colored_text(section_header.upper().replace("_", " "), color="TITLE")}\n{"=" * len(section_header)}', condition=self.use_json), filehandle=self.file_handler)

            # Enum dict per result list
            for idx, current_dictionary in enumerate(dict_list): # dict_list contain either all results if -gc or just current site result
                if self.grouping: # prints current url
                    ptmisclib.ptprint(ptmisclib.out_ifnot(ptmisclib.get_colored_text(f"{current_dictionary['url']}", 'INFO'), None, self.use_json), filehandle=self.file_handler)

                if section_header == "internal_urls_with_parameters":
                    self.print_parsed_urls(current_dictionary, dict_list)
                    continue

                if section_header == "metadata":
                    self.print_metadata(current_dictionary["data"][0]["metadata"], dict_list, idx)
                    continue

                if section_header == "metadata_tags":
                    if self.grouping_complete:
                        if not metadata_printed:
                            metadata_printed = True
                            merged_result = {"author": [], "robots": [], "generator": []}
                            for d in dict_list:
                                for key, value in d["data"][0]["metadata_tags"].items():
                                    merged_result[key] += value
                            for key, value in merged_result.items():
                                ptmisclib.ptprint(ptmisclib.out_ifnot(f"{key.capitalize()+('.'*(30-len(key)))}: {' :: '.join(value)}", "", self.use_json))
                    else:
                        for key, value in current_dictionary["data"][0]["metadata_tags"].items():
                            ptmisclib.ptprint(ptmisclib.out_ifnot(f"{key.capitalize()+('.'*(30-len(key)))}: {' :: '.join(value)}", "", self.use_json))
                        if self.grouping:
                            ptmisclib.ptprint(ptmisclib.out_ifnot(self.check_if_next(dict_list, idx, 'metadata_tags'), "", self.use_json), end="", filehandle=self.file_handler)
                    continue

                if section_header == "html_comments":
                    separator = "\n\n"

                if section_header == "forms":
                    if self.grouping_complete:
                        if not grouping_result and current_dictionary["data"][0]["forms"]:
                            grouping_result.append(current_dictionary["data"][0]["forms"][0])
                        for available_form in current_dictionary["data"][0]["forms"]:
                            form_is_already_included = False
                            available_form_without_value_keys = self.pop_value_key_from_form(available_form)
                            for already_included_form in grouping_result:
                                already_included_form_without_value_keys = self.pop_value_key_from_form(already_included_form)
                                if available_form_without_value_keys ==  already_included_form_without_value_keys:
                                    form_is_already_included = True
                                    break
                            if not form_is_already_included:
                                grouping_result.append(available_form)
                    else:
                        self.print_forms(current_dictionary["data"][0]["forms"])
                        if self.grouping and idx+1 != len(dict_list):
                            ptmisclib.ptprint(ptmisclib.out_ifnot(f" ", "", self.use_json))
                    continue

                if current_dictionary["data"][0].get(section_header) == ["Could not read file contents"] and self.grouping_complete:
                    continue

                if not current_dictionary["data"][0][section_header] and not self.grouping_complete:
                    ptmisclib.ptprint(ptmisclib.out_ifnot(f"Not found\n", "", self.use_json), end=self.check_if_next(dict_list, idx, section_header), filehandle=self.file_handler)
                    continue

                if self.grouping_complete:
                    if current_dictionary['data'][0].get(section_header):
                        for i in current_dictionary['data'][0][section_header]:
                            grouping_result.add(i)
                else:
                    ptmisclib.ptprint(ptmisclib.out_ifnot(separator.join(current_dictionary['data'][0][section_header]), condition=self.use_json), end=self.check_if_next(dict_list, idx, section_header)+"\n", filehandle=self.file_handler)

            if self.grouping_complete:
                # after all dictionaries iterated, unpack-print grouping result
                if section_header == "forms":
                    self.print_forms(grouping_result)
                    continue
                if section_header in ["metadata", "metadata_tags", "internal_urls_with_parameters"]:
                    continue
                if grouping_result:
                    ptmisclib.ptprint(ptmisclib.out_ifnot(separator.join(sorted(grouping_result)), condition=self.use_json), end=self.check_if_next(dict_list, idx, section_header)+"\n", filehandle=self.file_handler)
                else:
                    ptmisclib.ptprint(ptmisclib.out_ifnot(f"Not found\n", "", self.use_json), end=self.check_if_next(dict_list, idx, section_header), filehandle=self.file_handler)

            if self.output_parts:
                self.file_handler.close()

    def pop_value_key_from_form(self, form):
        """returns form without keys named 'value' (csrf tokens)"""
        form = copy.deepcopy(form)
        if form.get("inputs"):
            for parsed_input in form["inputs"]:
                if "value" in parsed_input.keys():
                    parsed_input.pop("value")
        return form

    def check_if_next(self, dict_list, index, section_header):
        try:
            endl = "\n" if dict_list[index+1]["data"][0].get(section_header) is not None else ""
        except Exception as e:
            endl = ""
        return endl

    def print_parsed_urls(self, current_dict, dict_list):
        for d in current_dict["data"][0]["internal_urls_with_parameters"]:
            ptmisclib.ptprint(ptmisclib.out_ifnot(f"URL: {d['url']}", "", self.use_json), filehandle=self.file_handler)
            ptmisclib.ptprint(ptmisclib.out_ifnot(f"Parameters:", "", self.use_json), filehandle=self.file_handler)
            for parameter in d['parameters']:
                    ptmisclib.ptprint(ptmisclib.out_ifnot('          ' + parameter), "\n", self.use_json, filehandle=self.file_handler)
            if len(dict_list) == 1:
                if d != current_dict["data"][0]["internal_urls_with_parameters"][-1]:
                    ptmisclib.ptprint(ptmisclib.out_ifnot(' '), "\n", self.use_json, filehandle=self.file_handler)
                else:
                    pass
            else:
                if current_dict["data"][0]["internal_urls_with_parameters"] == dict_list[-1]["data"][0]["internal_urls_with_parameters"] and d == current_dict["data"][0]["internal_urls_with_parameters"][-1]:
                    pass
                else:
                    ptmisclib.ptprint(ptmisclib.out_ifnot(' '), "\n", self.use_json, filehandle=self.file_handler)

    def print_forms(self, form_list):
        is_last = False
        for form in form_list:
            # is_last = last_form (without selects)
            if form == form_list[-1] and not form.get("selects"):
                is_last = True
            for key, value in form.items():
                space = 0 if key == "form_name" else 9
                if value == '':
                    value = "''"
                if key in ["inputs", "selects"]: # isinstance list
                    ptmisclib.ptprint(ptmisclib.out_ifnot(f" ", "", self.use_json), filehandle=self.file_handler)
                    if not form[key]:
                        continue

                    ptmisclib.ptprint(ptmisclib.out_ifnot(f"{' '*space}{key.title()}:", "", self.use_json), filehandle=self.file_handler)
                    space += len(key)

                    for index, dictionary in enumerate(form[key]):
                        for key2, value2 in dictionary.items():
                            if not value2 and value2 is not None:
                                value2 = "''"
                            if key2 == "options":
                                ptmisclib.ptprint(ptmisclib.out_ifnot(f"{' '*space}{key2.title()}:", "", self.use_json), filehandle=self.file_handler)
                                space += len(key)
                                for option in dictionary[key2]:
                                    if not option and option is not None:
                                        option = "''"
                                    ptmisclib.ptprint(ptmisclib.out_ifnot(f"{' '*space}{option}", "", self.use_json), filehandle=self.file_handler)
                                if self.grouping_complete and form != form_list[-1]:
                                    ptmisclib.ptprint(ptmisclib.out_ifnot(f" ", "", self.use_json), filehandle=self.file_handler)
                            else:
                                endl="\n"
                                if is_last and index+1 == len(form[key]) and key2 == list(dictionary.keys())[-1]:
                                    endl=""
                                ptmisclib.ptprint(ptmisclib.out_ifnot(f"{' '*space}{key2.title()}: {value2}", "", self.use_json), filehandle=self.file_handler, end=endl)
                        if index+1 != len(form[key]):
                            ptmisclib.ptprint(ptmisclib.out_ifnot(f" ", "", self.use_json), filehandle=self.file_handler)
                else:
                    ptmisclib.ptprint(ptmisclib.out_ifnot(f"{' '*space}{key.title().replace('_',' ')}: {value}", "", self.use_json), filehandle=self.file_handler)

    def print_metadata(self, metadata, dict_list, idx):
        for data, value in metadata.items():
            value = str(value).replace("\n", "\\n")
            ptmisclib.ptprint(ptmisclib.out_ifnot(f"{data}{'.'*(30-len(data))}: {value}", "", self.use_json), filehandle=self.file_handler)
        ptmisclib.ptprint(ptmisclib.out_ifnot(self.check_if_next(dict_list, idx, 'metadata'), "", self.use_json), end="", filehandle=self.file_handler)
        if self.grouping_complete:
            pass

    def _find(self, page_content, re_pattern):
        """Find and return list of all occurences of *re_pattern* in *page_content*"""
        result = list(set(i for i in re.finditer(re_pattern, page_content)))
        result = list(set(result.group(0) for result in re.finditer(re_pattern, page_content)))
        if result and type(result[0]) == tuple:
            result = self.tuplelist_to_stringlist(result)
        result = list(set(result for result in result))
        return result

    def get_soup(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        bdos = soup.find_all("bdo", {"dir": "rtl"})
        for item in bdos:
            item.string.replace_with(item.text[::-1])
        return soup

    def rel2abs(self, url, domain):
        if not domain.endswith("/") and not url.startswith("/"):
            domain += "/"
        if url.startswith("http://") | url.startswith("https://") | url.startswith("ftp://") | url.startswith("ftps://") | url.startswith("irc://"):
            return url
        else:
            return domain + url

    def tuplelist_to_stringlist(self, tuplelist, num_tuple_part=False):
        stringlist = []
        for tup in tuplelist:
            if num_tuple_part:
                stringlist.append("".join(tup[num_tuple_part]))
            else:
                stringlist.append("".join(tup))
        return stringlist

    def get_forms(self, soup):
        """Returns parsed page forms"""
        allowed_elements = ["form", "input", "select", "textarea", "label", "button", "datalist", "output"]
        forms = soup.find_all("form")
        forms_result = []
        for form in forms:
            form_elements = self.strip_form_elements(form.find_all(allowed_elements))
            forms_result.append({"form_name": form.get("name"), "action": form.get("action"), "method": form.get("method"), "form_id": form.get("id"),
            "inputs": [{"tag": ele.name, **ele.attrs} for ele in form_elements["inputs"]], "selects": [{"tag": ele.name, **ele.attrs} for ele in form_elements["selects"]]})
        return forms_result

    def strip_form_elements(self, form_elements):
        """strip child elements of parent element"""
        allowed_attrs = ("name", "type", "id", "value")
        result = {"inputs": [], "selects": []}
        for element in form_elements:
            element.attrs = {key: value for key, value in element.attrs.items() if key in allowed_attrs}
            if element.name == "select":
                element.attrs.update({"options": []})
            children = element.findChildren(True, recursive=True)
            for child in children:
                if child.name == "option":
                    element.attrs["options"].append(child.get("value", "notfound"))
                else:
                    child.unwrap()
            if element.name == "select":
                result["selects"].append(element)
            else:
                result["inputs"].append(element)
        return result

    def find_internal_parameters(self, internal_urls):
        parsed_urls = []
        for url in internal_urls:
            o = urllib.parse.urlsplit(url)
            if o.query:
                query_list = o.query.split("&")
                parsed_url = urllib.parse.urlunsplit((o[0], o[1], o[2], "", ""))
                result_data = {"url": parsed_url, "parameters": query_list}
                if not self.group_parameters:
                    parsed_urls.append(result_data)
                else:
                    if not parsed_urls:
                        parsed_urls.append(result_data)
                        continue
                    found = False
                    for d in parsed_urls:
                        if parsed_url == d["url"]:
                            d["parameters"].append(query_list)
                            found = True
                    if not found:
                        parsed_urls.append(result_data)
        return parsed_urls

    def _get_domain(self, domain):
        if domain and not re.match("https?:\/\/", domain):
            ptmisclib.end_error("Scheme required for --domain parameter", self.json_no, self.ptjsonlib, self.use_json)
        if domain and not domain.endswith("/"):
            domain += "/"
        return domain

    def _get_url_list(self, args):
        if not args.url and not args.file:
            ptmisclib.end_error("--url or --file parameter required", self.json_no, self.ptjsonlib, self.use_json)
        if args.url and args.file:
            ptmisclib.end_error("Cannot use --url and --file parameter together", self.json_no, self.ptjsonlib, self.use_json)
        if args.file:
            try:
                url_list = self.read_file(args.file)
            except FileNotFoundError:
                ptmisclib.end_error(f"File not found {os.path.join(os.getcwd(), args.file)}", self.json_no, self.ptjsonlib, self.use_json)
        elif args.url:
            url_list = args.url
        return url_list

    def get_extract_types(self, extract_str):
        allowed_letters = {
            "E": "emails",
            "S": "subdomains",
            "C": "html_comments",
            "F": "forms",
            "U": "internal_urls",
            "X": "external_urls",
            "P": "phone_numbers",
            "M": "metadata",
            "T": "tags",
            "I": "ip_addresses",
            "Q": "internal_urls_with_parameters",
            "A": "all"
        }
        extract_types = {
            "emails": None,
            "html_comments": None,
            "forms": None,
            "internal_urls": None,
            "external_urls": None,
            "internal_urls_with_parameters": None,
            "phone_numbers": None,
            "ip_addresses": None,
            "metadata": None,
            "tags": None,
            "subdomains": None,
            "all": None,
        }
        for char in extract_str:
            if char in allowed_letters.keys():
                extract_types.update({allowed_letters[char]: True})
                if char == "A":
                    for i in extract_types:
                        extract_types[i] = True
                    break
            else:
                ptmisclib.end_error(f"Invalid parameter '{char}' in --extract argument, allowed characters ({''.join(allowed_letters.keys())})", self.json_no, self.ptjsonlib, self.use_json)
        return extract_types

    def read_file(self, file):
        target_list = []
        with open(file, "r") as f:
            for line in f:
                line = line.strip("\n")
                if re.match('https?:\/\/', line):
                    target_list.append(line)
                elif self.domain:
                    if line.startswith("/"):
                        line = line[1:]
                    target_list.append(self.domain + line)
                else:
                    # continue
                    target_list.append(line)
            return target_list

def get_help():
    return [
        {"description": ["Web sources information extractor"]},
        {"usage": ["ptinsearcher <options>"]},
        {"usage_example": [
            "ptinsearcher -u https://www.example.com/",
            "ptinsearcher -u https://www.example.com/ -e H",
            "ptinsearcher -u https://www.example.com/ -e HSE",
            "ptinsearcher -f urlList.txt",
            "ptinsearcher -f urlList.txt -gc -e E",
        ]},
        {"options": [
            ["-u",  "--url",                   "<url>",            "Test URL"],
            ["-f",  "--file",                  "<file>",           "Load URL list from file"],
            ["-d",  "--domain",                "<domain>",         "Domain - Merge domain with filepath. Use when wordlist contains filepaths (e.g. /index.php)"],
            ["-e",  "--extract",               "<extract>",        "Specify data to extract [A, E, S, C, F, I, P, U, Q, X, M, T] (default A)"],
            ["", "-e A",                       "",                 "Extract All"],
            ["", "-e E",                       "",                 "Extract Emails"],
            ["", "-e S",                       "",                 "Extract Subdomains"],
            ["", "-e C",                       "",                 "Extract Comments"],
            ["", "-e F",                       "",                 "Extract Forms"],
            ["", "-e I",                       "",                 "Extract IP addresses"],
            ["", "-e P",                       "",                 "Extract Phone numbers"],
            ["", "-e U",                       "",                 "Extract Internal urls"],
            ["", "-e Q",                       "",                 "Extract Internal urls with parameters"],
            ["", "-e X",                       "",                 "Extract External urls"],
            ["", "-e M",                       "",                 "Extract Metadata"],
            ["", "-e T",                       "",                 "Extract Metadata-Tags (author, robots, generator)"],
            ["-o",  "--output",                "<output>",         "Save output to file"],
            ["-op", "--output-parts",          "",                 "Save each extract_type to separatorarate file"],
            ["-gp", "--group-parameters",      "",                 "Group URL parameters"],
            ["-wp", "--without-parameters",    "",                 "Without URL parameters"],
            ["-g",  "--grouping",              "",                 "One output table for all sites"],
            ["-gc",  "--grouping-complete",    "",                 "Merge all results into one group"],
            ["-r",  "--redirect",              "",                 "Follow redirects (default False)"],
            ["-c",  "--cookie",                "<cookie=value>",   "Set cookie(s)"],
            ["-H",  "--headers",               "<header:value>",   "Set custom headers"],
            ["-p",  "--proxy",                 "<proxy>",          "Set proxy (e.g. http://127.0.0.1:8080)"],
            ["-ua", "--user-agent",            "<user-agent>",     "Set User-Agent (default Penterep Tools)"],
            ["-j",  "--json",                  "",                 "Output in JSON format"],
            ["-v",  "--version",               "",                 "Show script version and exit"],
            ["-h",  "--help",                  "",                 "Show this help message and exit"]
        ]
        }]


def parse_args():
    parser = argparse.ArgumentParser(add_help=False, usage=f"{SCRIPTNAME} <options>")
    parser.add_argument("-u", "--url", type=str, nargs="+")
    parser.add_argument("-d", "--domain", type=str)
    parser.add_argument("-f", "--file", type=str)
    parser.add_argument("-e", "--extract", type=str, default="A")
    parser.add_argument("-pd", "--post-data", type=str)
    parser.add_argument("-r", "--redirects", action="store_true")
    parser.add_argument("-o", "--output", type=str)
    parser.add_argument("-op", "--output-parts", action="store_true")
    parser.add_argument("-g", "--grouping", action="store_true")
    parser.add_argument("-gc", "--grouping-complete", action="store_true")
    parser.add_argument("-gp", "--group-parameters", action="store_true")
    parser.add_argument("-wp", "--without-parameters", action="store_true")
    parser.add_argument("-p", "--proxy", type=str)
    parser.add_argument("-c", "--cookie", type=str, nargs="+")
    parser.add_argument("-H", "--headers", type=ptmisclib.pairs, nargs="+")
    parser.add_argument("-ua", "--user-agent", type=str, default="Penterep Tools")
    parser.add_argument("-j", "--json", action="store_true")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}", help="show version")

    if len(sys.argv) == 1 or "-h" in sys.argv or "--help" in sys.argv:
        ptmisclib.help_print(get_help(), SCRIPTNAME, __version__)
        sys.exit(0)
    args = parser.parse_args()
    ptmisclib.print_banner(SCRIPTNAME, __version__, args.json)
    return args


def main():
    global SCRIPTNAME
    SCRIPTNAME = "ptinsearcher"
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    args = parse_args()
    script = ptinsearcher(args)
    script.run(args)


if __name__ == "__main__":
    main()
