from sortedcontainers import SortedDict

menu = {
    "main": SortedDict(
        {
            100: SortedDict(
                {
                    100: ["dashboard", "Dashboard", "user-circle"],
                }
            ),
            200: SortedDict(
                {
                    100: ["account", "Account", "user-group"],
                    200: ["change_password", "Change Password", "key"],
                }
            ),
            999: SortedDict(
                {
                    100: ["sign_out", "Sign Out", "logout"],
                }
            ),
        }
    ),
}
