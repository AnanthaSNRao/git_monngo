import git_response_repo as repo
import sample_git_api as api
def main():
    response = api.SampleGitApi().getUser()
    res = repo.GitResponseRepo().save_response(response)
    if res:
        print("saved")
    else:
        print("not saved")

if __name__ == "__main__":
    main()