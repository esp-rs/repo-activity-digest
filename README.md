# repo-activity-digest

Automatically generates HTML digests for all configured repositories using [dinghy](https://github.com/nedbat/dinghy). A workflow runs every day at midnight UTC which generates and deploys the digests. Each digest shows the activity for a repository over the last 7 days.

## Quickstart

To generate the files locally:

```bash
$ python -m pip venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
$ ./generate.py
$ GITHUB_TOKEN="YOUR-GITHUB-TOKEN" python -m dinghy config.yaml
```

This will generate an HTML digest file for each repository listed in the `repositories.yml` file.

## License

Licensed under either of:

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in
the work by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without
any additional terms or conditions.
