from pybricks import version


def fw_version():
    """a python function to return the current firmware version"""
    return version


def split_string_on_char(s, split_char):
    """Split string with character as delimiter (synchronous)"""
    return s.split(split_char)


def report_git_hash(debug=False):
    """Return git hash from the firmware version"""
    hub_type, git_version, git_version_hash = fw_version()

    git_hash_list_spaces = split_string_on_char(git_version_hash, " ")
    git_date = git_hash_list_spaces[2]

    git_hash_list = split_string_on_char(git_hash_list_spaces[0], "-")
    if debug:
        print("git_hash_list", len(git_hash_list), git_hash_list)
    build_id = git_hash_list[2] if git_hash_list[1] == "build" else ""

    if len(git_hash_list) in [
        3,
        4,
    ]:  # 3.5.0 release, indicating a release version
        hash_type = " Release "
        git_hash = git_version
    else:  # assume 6 list elements
        hash_type = " with git hash "
        git_hash = split_string_on_char(git_hash_list[5], " ")[0]

        # Manually remove the first character without slicing (movehub has no slicing)
        _hash = ""
        for i in range(1, len(git_hash)):
            _hash += git_hash[i]
        git_hash = _hash
    # print("build_id", build_id)
    details = " from CI-build " + build_id if build_id != "" else ""
    # print("details", details)
    return (
        hub_type
        + hash_type
        + "'"
        + git_hash
        + " on "
        + git_date
        + "'"
        + details
    )
