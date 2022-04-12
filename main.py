from distutils.command.config import config
import mongo_data_handler
import fetch_data as data
import sys
import json

def main():
    f = open('./config.json')
    config = json.load(f)
    f.close()
    organization = config["COMPANY"]
    response_org_id  = data.fetch_git_data().get_organization(organization)

    # # reading from json payload
    # payload_repos = []
    # if response_org_id:
    #     for repo in payload_repos:
    #         ## 1
    #         issues_reposne = data.fetch_git_data().get_perceval_data("Issue", organization, repo, from_date, to_date)
    #         ## 2
    #         commit_reposne = data.fetch_git_data().get_commit_data(repo_url)

    # ## extract data from issues

    # count = mongo_data_handler.MongoDataHandler().extract_user_data_from_issues()
    # count1 = mongo_data_handler.MongoDataHandler().extract_user_data_from_commits()
    # print(count1)
    # print(count)




if __name__ == "__main__":
    main()