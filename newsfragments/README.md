This directory collects "newsfragments": short files that each contain
a snippet of ReST-formatted text that will be added to the next
release notes. This should be a description of aspects of the change
(if any) that are relevant to users. (This contrasts with the
commit message and PR description, which are a description of the change as
relevant to people working on the code itself.)

Each file should be named like `<ISSUE>.<TYPE>.rst`, where
`<ISSUE>` is an issue number, and `<TYPE>` is one of:

- `breaking`
- `bugfix`
- `deprecation`
- `docs`
- `feature`
- `internal`
- `misc`
- `performance`
- `removal`

So for example: `123.feature.rst`, `456.bugfix.rst`

All Pull Requests must address an existing issue. If there is no issue,
please open one first before submitting your changes. Use the issue
number for the newsfragment filename.

Note that the `towncrier` tool will automatically
reflow your text, so don't try to do any fancy formatting. Run
`towncrier build --draft` to get a preview of what the release notes entry
will look like in the final release notes.
