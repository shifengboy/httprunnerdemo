# NOTE: Generated By HttpRunner v3.1.4
# FROM: har/httprunnerdemo.har
import pytest
from httprunner import Parameters
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.mubu_login_test import TestCaseMubuLongin as MubuLongin


class TestCaseMubuCreateDocument(HttpRunner):

    @pytest.mark.parametrize("param",Parameters(
        {
        "folderId":["2KXaInOcEiV","qqQ0f4gn_V"],
        "memberId":["7722828074641062","7722828074641063"]
        }),
    )
    def test_start(self, param):
        super(TestCaseMubuCreateDocument, self).test_start(param)
    # 全局变量
    config = Config("testcase description") \
        .base_url("https://api2.${host}") \
        .verify(False) \
        .variables(**{
        "data_unique_id": "63743813-8230-4b9c-bb5a-f42416b1bbbf",
        "csrf_token": "bd41907d-ce86-41a5-a207-7b3d76aba3ab",
        "memberId": "7722828074641062",
        "host": "${get_test_host()}",
        # "phone": "13966566216",
        # "password": "chen123789",
        "folderId": "qqQ0f4gn_V"
    })

    teststeps = [
        Step(
            RunTestCase("login")
            .with_variables(**{
                "phone": "13966566216",
                "password": "chen123789",
            })
            .call(MubuLongin)
            .export("Jwt_Token", "user_persistence", "userId")
        ),
        Step(
            RunRequest("/v3/api/list/get_all_documents_page")
                .post("/v3/api/list/get_all_documents_page")
                .with_headers(
                **{
                    "content-length": "12",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"start": ""})
                .teardown_hook("${get_documents_num($response)}", "documents_num")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_greater_than("$documents_num", 2)
        ),
        Step(
            RunRequest("/v3/api/list/star_relation/get")
                .get("/v3/api/list/star_relation/get")
                .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
                .post("/v3/api/list/item_count")
                .with_headers(
                **{
                    "content-length": "30",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"folderId": 0, "source": "home"})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_user_params")
                .post("/v3/api/user/get_user_params")
                .with_headers(
                **{
                    "content-length": "0",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_data("")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/advertisement/get")
                .post("/v3/api/advertisement/get")
                .with_headers(
                **{
                    "content-length": "10",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"type": 1})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
                .post("/v3/api/list/item_count")
                .with_headers(
                **{
                    "content-length": "30",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"folderId": 0, "source": "home"})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        # Step(
        #     RunRequest("/v3/api/list/create_folder")
        #     .post("/v3/api/list/create_folder")
        #     .with_headers(
        #         **{
        #             "content-length": "38",
        #             "accept": "application/json, text/plain, */*",
        #             "jwt-token": "${Jwt_Token}",
        #             "content-type": "application/json;charset=UTF-8",
        #             "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        #             "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
        #             "x-request-id": "${get_random_request_id()}",
        #             "version": "3.0.0",
        #             "origin": "https://${host}",
        #             "sec-fetch-site": "same-site",
        #             "sec-fetch-mode": "cors",
        #             "sec-fetch-dest": "empty",
        #             "referer": "https://${host}/",
        #             "accept-encoding": "gzip, deflate, br",
        #             "accept-language": "zh-CN,zh;q=0.9",
        #         }
        #     )
        #     .with_json({"name": "shifeng_demo", "folderId": "0"})
        #     .extract()
        #     .with_jmespath("body.data.folder.id", "folderId")
        #     .validate()
        #     .assert_equal("status_code", 200)
        #     .assert_equal("body.code", 0)
        # ),
        Step(
            RunRequest("/v3/api/list/create_doc")
                .post("/v3/api/list/create_doc")
                .with_headers(
                **{
                    "content-length": "35",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"folderId": "${folderId}", "type": 0})
                .extract()
                .with_jmespath("body.data.id", "docId")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
                .post("/v3/api/list/item_count")
                .with_headers(
                **{
                    "content-length": "30",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"folderId": 0, "source": "home"})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/current_level")
                .post("/v3/api/user/current_level")
                .with_headers(
                **{
                    "content-length": "29",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"document_id": "${docId}"})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/document/edit/get")
                .post("/v3/api/document/edit/get")
                .with_headers(
                **{
                    "content-length": "37",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"docId": "${docId}", "password": ""})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/register")
                .get("/v3/api/colla/register")
                .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_invite_count")
                .get("/v3/api/user/get_invite_count")
                .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/members")
                .options("/v3/api/colla/members")
                .with_params(
                **{"memberId": "${memberId}", "documentId": "${docId}"}
            )
                .with_headers(
                **{
                    "accept": "*/*",
                    "access-control-request-method": "GET",
                    "access-control-request-headers": "data-unique-id,jwt-token,request-id,x-request-id",
                    "origin": "https://${host}",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/colla/members")
                .get("/v3/api/colla/members")
                .with_params(
                **{"memberId": "${memberId}", "documentId": "${docId}"}
            )
                .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "request-id": "members:${memberId}:1607862291799",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "x-request-id": "${get_random_request_id()}",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "489",
                    "member-id": "${memberId}",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "request-id": "MESSAGE:${userId}:${memberId}:9",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 9,
                    "requestId": "MESSAGE:${userId}:${memberId}:9",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 3,
                            "content": [
                                {
                                    "name": "nameChanged",
                                    "title": "${gen_random_string(10)}",
                                    "original": "",
                                },
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.16.0",
                        "appVersion": "2.0.0.373",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "461",
                    "member-id": "${memberId}",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "request-id": "MESSAGE:${userId}:${memberId}:10",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 10,
                    "requestId": "MESSAGE:${userId}:${memberId}:10",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 4,
                            "content": [
                                {
                                    "name": "create",
                                    "created": [
                                        {
                                            "index": 0,
                                            "parentId": None,
                                            "node": {
                                                "id": "j2N9mKu8Oz",
                                                "text": "demotext",
                                                "modified": 1607862297705,
                                                "children": [],
                                            },
                                            "path": ["nodes", 0],
                                        }
                                    ],
                                }
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.16.0",
                        "appVersion": "2.0.0.373",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "530",
                    "member-id": "${memberId}",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "request-id": "MESSAGE:${userId}:${memberId}:19",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 19,
                    "requestId": "MESSAGE:${userId}:${memberId}:19",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 9,
                            "content": [
                                {
                                    "name": "update",
                                    "updated": [
                                        {
                                            "updated": {
                                                "id": "j2N9mKu8Oz",
                                                "text": "<span>demotext</span>",
                                                "modified": 1607862301282,
                                            },
                                            "original": {
                                                "id": "j2N9mKu8Oz",
                                                "text": "<span>demote</span>",
                                                "modified": 1607862300148,
                                            },
                                            "path": ["nodes", 0],
                                        }
                                    ],
                                }
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.16.0",
                        "appVersion": "2.0.0.373",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "462",
                    "member-id": "${memberId}",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                    "data-unique-id": "59cf2860-3d3d-11eb-bad8-7f7b66d6f90f",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${Jwt_Token}",
                    "request-id": "MESSAGE:${userId}:${memberId}:21",
                    "x-request-id": "${get_random_request_id()}",
                    "version": "3.0.0",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 21,
                    "requestId": "MESSAGE:${userId}:${memberId}:21",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 10,
                            "content": [
                                {
                                    "name": "create",
                                    "created": [
                                        {
                                            "index": 1,
                                            "parentId": None,
                                            "node": {
                                                "id": "KEthtU8Cf4",
                                                "text": "<span>1111111</span>",
                                                "modified": 1607862302116,
                                                "children": [],
                                            },
                                            "path": ["nodes", 1],
                                        }
                                    ],
                                }
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.16.0",
                        "appVersion": "2.0.0.373",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),

    ]


if __name__ == "__main__":
    TestCaseMubuCreateDocument().test_start()
