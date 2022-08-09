# repo-activity-digest

Automatically generates HTML digests for all repositories in the `esp-rs` organization (which are **not** private and/or archived) using [dinghy](https://github.com/nedbat/dinghy). A workflow runs every day at midnight UTC which generates and deploys the digests. Each digest shows the activity for a repository over the last 7 days.

## Quickstart

To generate the files locally:

```bash
$ python -m pip venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
$ ./generate.py
$ GITHUB_TOKEN="YOUR-GITHUB-TOKEN" python -m dinghy config.yaml
```

This will generate an HTML digest file for each repository in the `esp-rs` organization, as well as an HTML index linking to each digest.

## License

Licensed under either of:

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in
the work by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without
any additional terms or conditions.
