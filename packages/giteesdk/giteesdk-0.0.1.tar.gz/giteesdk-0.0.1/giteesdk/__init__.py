#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import requests
import envx
default_scope = 'user_info projects pull_requests issues notes keys hook groups gists enterprises'
default_grant_type = 'password'
default_affiliation = 'owner, collaborator, organization_member, enterprise_member, admin'


class Basic:
    """
    文档：https://gitee.com/api/v5/swagger
    """
    def __init__(
            self,
            env_file_name: str = 'gitee.env'
    ):
        local_env = envx.read(env_file_name)
        self.username = local_env.get('username')
        self.password = local_env.get('password')
        self.client_id = local_env.get('client_id')
        self.client_secret = local_env.get('client_secret')
        self.scope = local_env.get('scope', default_scope)
        self.grant_type = local_env.get('grant_type', default_grant_type)

        self.oauth_res = self.oauth()
        self.access_token = self.oauth_res.get('access_token')  # 用户授权码

    def oauth(
            self
    ):
        """
        密码模式，参照文档：https://gitee.com/api/v5/oauth_doc#/list-item-1
        返回：
        {
            'access_token': '......',
            'token_type': 'bearer',
            'expires_in': 86400,
            'refresh_token': '..............',
            'scope': 'user_infoprojectspull_requestsissuesnoteskeyshookgroupsgistsenterprises',
            'created_at': 1638462297
        }
        """
        url = 'https://gitee.com/oauth/token'
        data = {
            'username': self.username,
            'password': self.password,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': self.scope,
            'grant_type': self.grant_type,
        }
        response = requests.post(
            url=url,
            data=data
        )
        return response.json()

    def enterprises(
            self,
            page: int = 1,
            per_page: int = 20,
            get_all: bool = False,
            admin: bool = False  # 只列出授权用户管理的企业
    ):
        """
        列出授权用户所属的企业
        文档：https://gitee.com/api/v5/swagger#/getV5UserEnterprises
        """
        url = 'https://gitee.com/api/v5/user/enterprises'
        response_json_all = list()
        while True:
            data = {
                'access_token': self.access_token,
                'page': page,  # 当前的页码
                'per_page': per_page,  # 每页的数量，最大为 100
                'admin': admin  # 只列出授权用户管理的企业
            }
            response = requests.get(
                url=url,
                data=data
            )
            response_json_all.extend(response.json())
            response_headers = response.headers
            total_page = int(response_headers.get('total_page', '1'))
            if page >= total_page:
                break
            else:
                if get_all is False:
                    break
                else:
                    page += 1
        return response_json_all

    def orgs(
            self,
            page: int = 1,
            per_page: int = 20,
            get_all: bool = False,
            admin: bool = False  # 只列出授权用户管理的企业
    ):
        """
        列出授权用户所属的组织
        文档：https://gitee.com/api/v5/swagger#/getV5UserOrgs
        """
        url = 'https://gitee.com/api/v5/user/orgs'
        response_json_all = list()
        while True:
            data = {
                'access_token': self.access_token,
                'page': page,  # 当前的页码
                'per_page': per_page,  # 每页的数量，最大为 100
                'admin': admin  # 只列出授权用户管理的组织
            }
            response = requests.get(
                url=url,
                data=data
            )
            response_json_all.extend(response.json())
            response_headers = response.headers
            total_page = int(response_headers.get('total_page', '1'))
            if page >= total_page:
                break
            else:
                if get_all is False:
                    break
                else:
                    page += 1
        return response_json_all

    def repos(
            self,
            page: int = 1,  # 当前的页码
            per_page: int = 20,  # 每页的数量，最大为 100
            get_all: bool = False,
            visibility: str = 'all',  # 公开(public)、私有(private)或者所有(all)，默认: 所有(all)
            affiliation: str = default_affiliation,  # owner(授权用户拥有的仓库)、collaborator(授权用户为仓库成员)、organization_member(授权用户为仓库所在组织并有访问仓库权限)、enterprise_member(授权用户所在企业并有访问仓库权限)、admin(所有有权限的，包括所管理的组织中所有仓库、所管理的企业的所有仓库)。 可以用逗号分隔符组合。如: owner, organization_member 或 owner, collaborator, organization_member
            _type: str = None,  # 筛选用户仓库: 其创建(owner)、个人(personal)、其为成员(member)、公开(public)、私有(private)，不能与 visibility 或 affiliation 参数一并使用，否则会报 422 错误
            _sort: str = 'full_name',  # 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name
            direction: str = None,  # 如果sort参数为full_name，用升序(asc)。否则降序(desc)
            q: str = None,  # 搜索关键字
    ):
        """
        列出授权用户的所有仓库
        文档：https://gitee.com/api/v5/swagger#/getV5UserRepos
        """
        url = 'https://gitee.com/api/v5/user/repos'
        response_json_all = list()
        while True:
            data = {
                'access_token': self.access_token,
                'visibility': visibility,
                'affiliation': affiliation,
                'sort': _sort,
                'page': page,
                'per_page': per_page,
            }
            if _type is not None:
                data['type'] = _type

            if direction is not None:
                data['direction'] = direction

            if q is not None:
                data['q'] = q

            response = requests.get(
                url=url,
                data=data
            )
            response_json_all.extend(response.json())
            response_headers = response.headers
            total_page = int(response_headers.get('total_page', '1'))
            if page >= total_page:
                break
            else:
                if get_all is False:
                    break
                else:
                    page += 1
        return response_json_all
