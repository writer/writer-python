# Changelog

## 2.3.2-rc2 (2025-10-01)

Full Changelog: [v2.3.2-rc1...v2.3.2-rc2](https://github.com/writer/writer-python/compare/v2.3.2-rc1...v2.3.2-rc2)

### Features

* **api:** manual updates ([4fb84e2](https://github.com/writer/writer-python/commit/4fb84e2d911b8a32a2fc34bb88bcd7ac7b15d2f2))
* **api:** manual updates ([d7b4637](https://github.com/writer/writer-python/commit/d7b463727d2d9b3cd90fcab9e7d5376a3d5a1a38))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([7912ae2](https://github.com/writer/writer-python/commit/7912ae28b073194868bbcdc59bbff92b49a50f60))
* **internal:** update pydantic dependency ([c2f8537](https://github.com/writer/writer-python/commit/c2f85373ed1ed9e0e80a3b3d182794dc619d8b87))
* **types:** change optional parameter type from NotGiven to Omit ([702d003](https://github.com/writer/writer-python/commit/702d003ebd5c955986898f7afadc425f9a9c4fd1))
* update more locations to use Omit ([5f1a99c](https://github.com/writer/writer-python/commit/5f1a99c3546308523ce977ce3bf1f145209ad44b))


### Documentation

* **api:** updates to API spec ([7e349a9](https://github.com/writer/writer-python/commit/7e349a9c9782b10803ef932ee7eaf9c618750d2b))

## 2.3.2-rc1 (2025-09-11)

Full Changelog: [v2.3.1...v2.3.2-rc1](https://github.com/writer/writer-python/compare/v2.3.1...v2.3.2-rc1)

### Features

* improve future compat with pydantic v3 ([74315c4](https://github.com/writer/writer-python/commit/74315c493b0f439614d492378ae34fc0728c8bb1))
* **types:** replace List[str] with SequenceNotStr in params ([2c1a7de](https://github.com/writer/writer-python/commit/2c1a7de9a61c13b20b7734ba4f87da6ca7771e30))


### Bug Fixes

* avoid newer type syntax ([4aec590](https://github.com/writer/writer-python/commit/4aec5902d7329039817f2049c299458fa8eb1381))
* **client:** custom patch to prepare pydantic v3 ([8a26e46](https://github.com/writer/writer-python/commit/8a26e46ec365ea9905be7531bd80ebd9c74b129d))


### Chores

* **client:** format ([fa024a5](https://github.com/writer/writer-python/commit/fa024a58b0bc88104744f17279f5ca3819f28284))
* **client:** update stop params in stream/parse to match chat ([8920408](https://github.com/writer/writer-python/commit/8920408285a5adfe7d0a416bc4539e42326b180e))
* **internal:** add Sequence related utils ([40901e2](https://github.com/writer/writer-python/commit/40901e2ad2c45f6d8258df2e0666cc88c6c1fa0f))
* **internal:** change ci workflow machines ([84dcbed](https://github.com/writer/writer-python/commit/84dcbedf80ab51ed3d4379839682b0c584041bb9))
* **internal:** move mypy configurations to `pyproject.toml` file ([2518950](https://github.com/writer/writer-python/commit/251895049da0d7302cb37c599b0ca23dd0b6d470))
* **internal:** update pyright exclude list ([815b794](https://github.com/writer/writer-python/commit/815b794df77ae9e20842db345988c93f1f077ee7))
* **tests:** simplify `get_platform` test ([f1ddbb2](https://github.com/writer/writer-python/commit/f1ddbb236dbc6c1780eb1120e2fba20c0e4c921a))
* update github action ([d81d1ec](https://github.com/writer/writer-python/commit/d81d1ec4fe56a7761fd5c3ad2afc65e8b12954fd))


### Documentation

* **api:** updates to API spec ([daf31d5](https://github.com/writer/writer-python/commit/daf31d587a7bc32c9debe961ac870d08fedef865))
* **api:** updates to API spec ([5f8a109](https://github.com/writer/writer-python/commit/5f8a109801baff44a41313e2a4774ecc2c7e70bd))

## 2.3.1 (2025-08-20)

Full Changelog: [v2.3.1-rc1...v2.3.1](https://github.com/writer/writer-python/compare/v2.3.1-rc1...v2.3.1)

## 2.3.1-rc1 (2025-08-19)

Full Changelog: [v2.3.0...v2.3.1-rc1](https://github.com/writer/writer-python/compare/v2.3.0...v2.3.1-rc1)

### Documentation

* **api:** updates to API spec ([8f5acc8](https://github.com/writer/writer-python/commit/8f5acc859cef51375ed2abf641c7087a36d26e02))

## 2.3.0 (2025-08-14)

Full Changelog: [v2.3.0-rc1...v2.3.0](https://github.com/writer/writer-python/compare/v2.3.0-rc1...v2.3.0)

## 2.3.0-rc1 (2025-08-12)

Full Changelog: [v2.2.1...v2.3.0-rc1](https://github.com/writer/writer-python/compare/v2.2.1...v2.3.0-rc1)

### Features

* **api:** add web KG and web search ([127319b](https://github.com/writer/writer-python/commit/127319bf155e738a86e344330e3b59a252ae5bd3))
* **client:** support file upload requests ([aa0d06d](https://github.com/writer/writer-python/commit/aa0d06d2b73d9912a8542de146c8c0d0d0d150b2))


### Bug Fixes

* Add web_search_data to streaming tests. ([73f3db7](https://github.com/writer/writer-python/commit/73f3db7b36bde194d971afc2b16812b88e98e079))
* **parsing:** ignore empty metadata ([8874173](https://github.com/writer/writer-python/commit/8874173e4d0d73c1209bfedee5bb29b5d720c9ec))
* **parsing:** parse extra field types ([d1f5948](https://github.com/writer/writer-python/commit/d1f5948323742a54080dbd008532ce4be17289ba))


### Chores

* **internal:** fix ruff target version ([851522b](https://github.com/writer/writer-python/commit/851522bde50ed18925feb4d07191418be908e6ec))
* **internal:** update comment in script ([279d7df](https://github.com/writer/writer-python/commit/279d7df957f5fd0b75fcd6a4bbae84e79f1f1288))
* **project:** add settings file for vscode ([1c5e20c](https://github.com/writer/writer-python/commit/1c5e20ca653e671b71dc5b8e7d82db9a9dd2a51e))
* update @stainless-api/prism-cli to v5.15.0 ([cdbd4b3](https://github.com/writer/writer-python/commit/cdbd4b3a5551b96ecda64be222ef9ac89e527794))


### Documentation

* **api:** updates to API spec ([4482f85](https://github.com/writer/writer-python/commit/4482f8521bf9e126dbe1f51e298efb1b74b2c100))
* **api:** updates to API spec ([fe26f83](https://github.com/writer/writer-python/commit/fe26f8328201752961a0e1b7d3c418c357b0ccf7))
* **api:** updates to API spec ([a780648](https://github.com/writer/writer-python/commit/a780648ff3063801cdb349ad5cc275139e7726f9))

## 2.2.1 (2025-07-16)

Full Changelog: [v2.2.0...v2.2.1](https://github.com/writer/writer-python/compare/v2.2.0...v2.2.1)

### Features

* clean up environment call outs ([fc436af](https://github.com/writer/writer-python/commit/fc436af17d30723e147c0cc8198886adfa43d0a1))
* **client:** add follow_redirects request option ([1bf8218](https://github.com/writer/writer-python/commit/1bf8218881286ddf4bf1c9c2c4c8e8b58837425b))
* **client:** add support for aiohttp ([843d69d](https://github.com/writer/writer-python/commit/843d69decc9eb5c1cb793fc466c026917e8036ce))


### Bug Fixes

* allow utf-8 encoded filename in headers ([27ebc83](https://github.com/writer/writer-python/commit/27ebc83f9eb76b7ab2208ed8ac991bd857773928))
* **ci:** correct conditional ([7f49d8d](https://github.com/writer/writer-python/commit/7f49d8d55819747831db0b7baa015b274b18108d))
* **ci:** release-doctor — report correct token name ([0d20a9e](https://github.com/writer/writer-python/commit/0d20a9e7d8be4f8fbc316480335afd314d112a8a))
* **client:** correctly parse binary response | stream ([55872c2](https://github.com/writer/writer-python/commit/55872c2302ae5458f872ab34809c85781f0f6f17))
* **client:** don't send Content-Type header on GET requests ([ffcc579](https://github.com/writer/writer-python/commit/ffcc5799423bca552deabaa0cf98dc2e67d11a39))
* merged_headers -&gt; default_headers to avoid conflicts ([6b7aeb4](https://github.com/writer/writer-python/commit/6b7aeb4335534bcfafc2f9849fa4162f44002075))
* **package:** support direct resource imports ([2016cda](https://github.com/writer/writer-python/commit/2016cda2813d2b49abf8f6aa2dafbecdcaddfa36))
* **parsing:** correctly handle nested discriminated unions ([a4774a8](https://github.com/writer/writer-python/commit/a4774a8592d82d03ff1d2947ee61a909ac40d534))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([f5db115](https://github.com/writer/writer-python/commit/f5db1150f0c8b53e9c9b471c1b1f555cfa6be2df))


### Chores

* **ci:** change upload type ([9ee05fb](https://github.com/writer/writer-python/commit/9ee05fb02fede8fcba4418c55361080106f5172e))
* **ci:** enable for pull requests ([2dc262b](https://github.com/writer/writer-python/commit/2dc262bf297d3d0f42489cf2c3e2ea59cb1a17cc))
* **ci:** fix installation instructions ([b421fd0](https://github.com/writer/writer-python/commit/b421fd089015ede20a5cfa8214c19dc16b66f27c))
* **ci:** only run for pushes and fork pull requests ([ced5ec3](https://github.com/writer/writer-python/commit/ced5ec33765e4d8454c597a135d20be8b89e0c4e))
* **ci:** upload sdks to package manager ([bfc448f](https://github.com/writer/writer-python/commit/bfc448fb9516e07a3a5fa903ef04b2e838865a0a))
* **docs:** grammar improvements ([302e1a8](https://github.com/writer/writer-python/commit/302e1a8fb48a3f0fa83bef9fa1fb5ee2244893f1))
* **docs:** remove reference to rye shell ([b6a9aff](https://github.com/writer/writer-python/commit/b6a9aff0e0da58c0f19b4634448be6b6d539593c))
* **docs:** remove unnecessary param examples ([b78bf04](https://github.com/writer/writer-python/commit/b78bf04d813ce51075386f660a0cfa3647db77d3))
* **internal:** avoid errors for isinstance checks on proxies ([6bec701](https://github.com/writer/writer-python/commit/6bec701344af3c9cd7853cc9dcacfbd959dbf485))
* **internal:** avoid lint errors in pagination expressions ([abf0203](https://github.com/writer/writer-python/commit/abf02038a3857004cbb061cffaa9f0bf29f841b0))
* **internal:** bump pinned h11 dep ([383abab](https://github.com/writer/writer-python/commit/383ababb87995f734a70b58178d407b00df130ea))
* **internal:** codegen related update ([81c98bd](https://github.com/writer/writer-python/commit/81c98bd5948b7b5d0175134f43ced00a559d3f41))
* **internal:** update conftest.py ([f6aa1eb](https://github.com/writer/writer-python/commit/f6aa1eb979f08b6ee1f9518f19b618e9346c04c6))
* **package:** mark python 3.13 as supported ([fe9f5d9](https://github.com/writer/writer-python/commit/fe9f5d904f516d1eb37037acd07df4e43e86246a))
* parse environment variables for default headers ([fd7c358](https://github.com/writer/writer-python/commit/fd7c358ae9671a20c338d6868b4420b8a982fe17))
* **readme:** fix version rendering on pypi ([b93bb29](https://github.com/writer/writer-python/commit/b93bb292fe04ff647049ef0b1431181435463c92))
* **readme:** update badges ([52ec704](https://github.com/writer/writer-python/commit/52ec7049643a69006ad01aa7d3c47533e017afd9))
* **tests:** add tests for httpx client instantiation & proxies ([5e99c8f](https://github.com/writer/writer-python/commit/5e99c8fae8879b664c7982fc88a0f5dfd0f111d7))
* **tests:** run tests in parallel ([6c8b5ad](https://github.com/writer/writer-python/commit/6c8b5ad718480211ef16b7a81064eadb988c69de))
* **tests:** skip some failing tests on the latest python versions ([94bb5d6](https://github.com/writer/writer-python/commit/94bb5d63562691568da5e2a48e4890dbbbcda456))


### Documentation

* **api:** updates to API spec ([4902642](https://github.com/writer/writer-python/commit/4902642b8d9cc80b3bae1d5a10d44a0959e2d0b0))
* **api:** updates to API spec ([e704323](https://github.com/writer/writer-python/commit/e7043234b044b7fa0897c2f3d07685d429071c08))
* **client:** fix httpx.Timeout documentation reference ([f0cc6ef](https://github.com/writer/writer-python/commit/f0cc6ef6ac440627a7ed903142b79d49c3d0a22e))

## 2.2.0 (2025-04-30)

Full Changelog: [v2.2.0-rc1...v2.2.0](https://github.com/writer/writer-python/compare/v2.2.0-rc1...v2.2.0)

### Documentation

* **api:** updates to API spec ([0236e86](https://github.com/writer/writer-python/commit/0236e8698e48b393dbb711f91e76fef66007d724))
* README updates ([c85f8b5](https://github.com/writer/writer-python/commit/c85f8b591d27e4f0b2ff1ff01532aa31c4b62f7b))
* Update models in README. ([da7e11a](https://github.com/writer/writer-python/commit/da7e11a9c62d971253efc83550557be37864fabb))

## 2.2.0-rc1 (2025-04-25)

Full Changelog: [v2.1.0...v2.2.0-rc1](https://github.com/writer/writer-python/compare/v2.1.0...v2.2.0-rc1)

### Features

* **api:** add ai detect tool endpoint ([5155d78](https://github.com/writer/writer-python/commit/5155d7885097a4d62236c97d299db5b392c19c46))
* **api:** add translation endpoint ([c475528](https://github.com/writer/writer-python/commit/c475528d5d31a8cc2919b9d9315e3dd4d5fac9aa))
* **chat:** add parse method ([#237](https://github.com/writer/writer-python/issues/237)) ([81aae52](https://github.com/writer/writer-python/commit/81aae52c2dc0cc227dfa4b5e04d0b95140f40cbf))


### Bug Fixes

* **perf:** optimize some hot paths ([b1304d3](https://github.com/writer/writer-python/commit/b1304d306bb7e1e001de04d30be69adca53dbb63))
* **perf:** skip traversing types for NotGiven values ([db0383a](https://github.com/writer/writer-python/commit/db0383a6c77cb059eab8d0c48d1ef27842128d14))
* **pydantic v1:** more robust ModelField.annotation check ([fe810b2](https://github.com/writer/writer-python/commit/fe810b23a492ad0266e4f6ccb765946f92b2cee6))


### Chores

* broadly detect json family of content-type headers ([128b22a](https://github.com/writer/writer-python/commit/128b22aced2c242dc36e50b638db667febd56b09))
* **ci:** add timeout thresholds for CI jobs ([7e48fde](https://github.com/writer/writer-python/commit/7e48fde8c5e170e19a5ac3c6dcba6dccc2d592a2))
* **ci:** only use depot for staging repos ([4e41929](https://github.com/writer/writer-python/commit/4e41929b07a15cdf4041a5a6ca2f41d5281cfbc5))
* **ci:** run on more branches and use depot runners ([00cad5e](https://github.com/writer/writer-python/commit/00cad5e1a4b252d252a2c14f5631f65d9b3ce90c))
* **client:** minor internal fixes ([8f42cd8](https://github.com/writer/writer-python/commit/8f42cd864779a07e2f9401e1690d1f241e2dcb1a))
* **internal:** base client updates ([77cdb4a](https://github.com/writer/writer-python/commit/77cdb4aa35a6dc165bbf3e36b151377f25b77704))
* **internal:** bump pyright version ([bcd957a](https://github.com/writer/writer-python/commit/bcd957a67bface1dc31c111928cf2bf604df0b56))
* **internal:** expand CI branch coverage ([#235](https://github.com/writer/writer-python/issues/235)) ([672e10d](https://github.com/writer/writer-python/commit/672e10da46e802e25dce515311370c5faedf6721))
* **internal:** fix list file params ([d8f9820](https://github.com/writer/writer-python/commit/d8f98203056e0ded99fa8a05f43d30c3e3762ab3))
* **internal:** import reformatting ([3994040](https://github.com/writer/writer-python/commit/3994040da781e1c42eae00996609baffc8b04ee4))
* **internal:** minor formatting changes ([2064f80](https://github.com/writer/writer-python/commit/2064f80ff07f1d731bcbf5f02105777f153b2981))
* **internal:** reduce CI branch coverage ([725029b](https://github.com/writer/writer-python/commit/725029b1896669ea364ddc7795c0d4f3be56c890))
* **internal:** refactor retries to not use recursion ([acf730e](https://github.com/writer/writer-python/commit/acf730e5cf9b2b579338a03a6f90692c662544c1))
* **internal:** slight transform perf improvement ([#233](https://github.com/writer/writer-python/issues/233)) ([92b7914](https://github.com/writer/writer-python/commit/92b7914f583d680b6f85bee45a7177ca2b3a61ee))
* **internal:** update models test ([ba97e8f](https://github.com/writer/writer-python/commit/ba97e8f02e8e252cc11cacc46dfd30a73cb6ed43))
* **internal:** update pyright settings ([8f7e894](https://github.com/writer/writer-python/commit/8f7e89421ed0a77f814fb7810212d19f1d795ba9))


### Documentation

* **api:** updates to API spec ([fa87048](https://github.com/writer/writer-python/commit/fa870480b59f2b9bac562615c78c2c5d08932351))
* **api:** updates to API spec ([7606fe4](https://github.com/writer/writer-python/commit/7606fe4c32d1e28d84d0b10a951d3cfe030b8f84))
* **api:** updates to API spec ([a423a7e](https://github.com/writer/writer-python/commit/a423a7e58237a6202d9fafcd200e2f3cd79321bb))
* **api:** updates to API spec ([91598ac](https://github.com/writer/writer-python/commit/91598ac7aabbb3b94bfd28a46249e46b893f1d69))
* swap examples used in readme ([#231](https://github.com/writer/writer-python/issues/231)) ([e944c5b](https://github.com/writer/writer-python/commit/e944c5bf1cef967cb2de23ca844152d66f714b68))

## 2.1.0 (2025-04-04)

Full Changelog: [v2.1.0-rc1...v2.1.0](https://github.com/writer/writer-python/compare/v2.1.0-rc1...v2.1.0)

### Chores

* **internal:** remove trailing character ([#227](https://github.com/writer/writer-python/issues/227)) ([f8ad509](https://github.com/writer/writer-python/commit/f8ad509d1862bc7cb12f3890f0237510e8835168))
* **internal:** version bump ([#225](https://github.com/writer/writer-python/issues/225)) ([7df4049](https://github.com/writer/writer-python/commit/7df404939f19da3966b5daceffa914838f967894))

## 2.1.0-rc1 (2025-04-01)

Full Changelog: [v2.0.0...v2.1.0-rc1](https://github.com/writer/writer-python/compare/v2.0.0...v2.1.0-rc1)

### Features

* add chat streaming helpers ([#209](https://github.com/writer/writer-python/issues/209)) ([7b65fc1](https://github.com/writer/writer-python/commit/7b65fc1d54432bba101f1f23a83d532644a298be))
* **api:** Add Vision endpoint. ([#220](https://github.com/writer/writer-python/issues/220)) ([886b828](https://github.com/writer/writer-python/commit/886b82895a8dd336debafa588ac1e14da359677d))
* **api:** Add Vision endpoint. ([#221](https://github.com/writer/writer-python/issues/221)) ([967073d](https://github.com/writer/writer-python/commit/967073dec1241af76c0d11b4805c64f5ee7b7844))


### Bug Fixes

* **ci:** ensure pip is always available ([#214](https://github.com/writer/writer-python/issues/214)) ([7285bc1](https://github.com/writer/writer-python/commit/7285bc105f39631ce52d7877bc335d49cbe9294c))
* **ci:** remove publishing patch ([#215](https://github.com/writer/writer-python/issues/215)) ([26c3993](https://github.com/writer/writer-python/commit/26c39939db099741785c7f2cb013a8a5105c2273))
* **types:** handle more discriminated union shapes ([#213](https://github.com/writer/writer-python/issues/213)) ([d1a067c](https://github.com/writer/writer-python/commit/d1a067ce68afa9fb59832c291b1d9fbd30aae763))


### Chores

* **docs:** update client docstring ([#203](https://github.com/writer/writer-python/issues/203)) ([3779210](https://github.com/writer/writer-python/commit/3779210ed12a9332f86682059b4aec4320cf7e7c))
* fix typos ([#222](https://github.com/writer/writer-python/issues/222)) ([2ad9218](https://github.com/writer/writer-python/commit/2ad92187d04daa64d4dd0720d8cd941523c411c9))
* **internal:** bump rye to 0.44.0 ([#211](https://github.com/writer/writer-python/issues/211)) ([7efe8a4](https://github.com/writer/writer-python/commit/7efe8a4b003ea1d4edeee785e9f9ac805b914289))
* **internal:** codegen related update ([#204](https://github.com/writer/writer-python/issues/204)) ([f5e9ce7](https://github.com/writer/writer-python/commit/f5e9ce7c1a763fd59547b7eb1f5c0856dc80562b))
* **internal:** Fix README code samples. ([#219](https://github.com/writer/writer-python/issues/219)) ([2efd5ea](https://github.com/writer/writer-python/commit/2efd5eafe21865ea6406e463cdac2231c0f810ea))
* **internal:** Fix README samples. ([#217](https://github.com/writer/writer-python/issues/217)) ([a06f969](https://github.com/writer/writer-python/commit/a06f9697adf77ee2be877279179977270581d393))
* **internal:** remove extra empty newlines ([#210](https://github.com/writer/writer-python/issues/210)) ([3b5fd4c](https://github.com/writer/writer-python/commit/3b5fd4c429c740ca2f460b6f974769336831e80e))
* **internal:** version bump ([#200](https://github.com/writer/writer-python/issues/200)) ([a7b5f67](https://github.com/writer/writer-python/commit/a7b5f670838042af9a51c6e916ba0dff122635ce))


### Documentation

* **api:** updates to API spec ([#208](https://github.com/writer/writer-python/issues/208)) ([829e77a](https://github.com/writer/writer-python/commit/829e77ae9fb6e899fbdc6075586491404ef910da))
* **api:** updates to API spec ([#216](https://github.com/writer/writer-python/issues/216)) ([3d29c55](https://github.com/writer/writer-python/commit/3d29c5598266b8da7fe9aae0614dc4b43c4986f3))
* **api:** updates to API spec ([#223](https://github.com/writer/writer-python/issues/223)) ([c72a478](https://github.com/writer/writer-python/commit/c72a4781f221ecaba62519c1c08831ab78ee2169))
* **api:** updates to API spec ([#224](https://github.com/writer/writer-python/issues/224)) ([7a990d7](https://github.com/writer/writer-python/commit/7a990d7af74adaac7b68b0d2319e8abc3704c757))
* revise readme docs about nested params ([#206](https://github.com/writer/writer-python/issues/206)) ([ce4dfcc](https://github.com/writer/writer-python/commit/ce4dfcc857ae82c2d4cab789d32844d6643b2d56))
* update URLs from stainlessapi.com to stainless.com ([#202](https://github.com/writer/writer-python/issues/202)) ([5895a7a](https://github.com/writer/writer-python/commit/5895a7a2c077f50c74ee56c2e985f3ac7fa63382))

## 2.0.0 (2025-02-26)

Full Changelog: [v2.0.0-rc1...v2.0.0](https://github.com/writer/writer-python/compare/v2.0.0-rc1...v2.0.0)

### Chores

* **internal:** properly set __pydantic_private__ ([#197](https://github.com/writer/writer-python/issues/197)) ([533c0f8](https://github.com/writer/writer-python/commit/533c0f8c14ba78fb827fa494d25a4367612ad0fa))
* **internal:** version bump ([#194](https://github.com/writer/writer-python/issues/194)) ([f75756f](https://github.com/writer/writer-python/commit/f75756f03a1e2083fc9cc6be66596a19606d1312))


### Documentation

* Add file upload examples to README. ([#199](https://github.com/writer/writer-python/issues/199)) ([628cf7f](https://github.com/writer/writer-python/commit/628cf7f3a0047af764d31b156709443175806d59))
* **api:** updates to API spec ([#196](https://github.com/writer/writer-python/issues/196)) ([2867dbb](https://github.com/writer/writer-python/commit/2867dbbefe5b5795f043fc2641a5320e24bf0788))

## 2.0.0-rc1 (2025-02-21)

Full Changelog: [v1.6.1...v2.0.0-rc1](https://github.com/writer/writer-python/compare/v1.6.1...v2.0.0-rc1)

### ⚠ BREAKING CHANGES

* **api:** define chat completion models ([#157](https://github.com/writer/writer-python/issues/157))

### Features

* **api:** add async jobs and graph association ([#167](https://github.com/writer/writer-python/issues/167)) ([5ffd871](https://github.com/writer/writer-python/commit/5ffd8713d73630b38a7f2f3bdecce8c6ade4a29e))
* **api:** add list and retrieve applications ([#176](https://github.com/writer/writer-python/issues/176)) ([79e2193](https://github.com/writer/writer-python/commit/79e21937c92103b5d24b685d52cc04ecd63da172))
* **api:** add types for application jobs ([#171](https://github.com/writer/writer-python/issues/171)) ([e73ec53](https://github.com/writer/writer-python/commit/e73ec532074669f95ad79f02e33b3d56612a5c46))
* **api:** define chat completion models ([#157](https://github.com/writer/writer-python/issues/157)) ([2a1d32a](https://github.com/writer/writer-python/commit/2a1d32a64b8fb155fad130b4dd1d4966a5451bd9))
* **api:** update application jobs pagination response ([#169](https://github.com/writer/writer-python/issues/169)) ([cb30cef](https://github.com/writer/writer-python/commit/cb30cef03042508722c6ab2f07aca3f9b5d3369f))
* **client:** allow passing `NotGiven` for body ([#187](https://github.com/writer/writer-python/issues/187)) ([b179ebb](https://github.com/writer/writer-python/commit/b179ebbee68645ca29e21971536444b7f7f45e7f))
* **client:** send `X-Stainless-Read-Timeout` header ([#175](https://github.com/writer/writer-python/issues/175)) ([2f6ceb9](https://github.com/writer/writer-python/commit/2f6ceb9f27103cfc5df7a8976c8bf2aa0161aa7b))


### Bug Fixes

* **api:** fix offset pagination schema ([#177](https://github.com/writer/writer-python/issues/177)) ([fca1562](https://github.com/writer/writer-python/commit/fca156251459a169658a487b0f88bcdefae363d0))
* asyncify on non-asyncio runtimes ([#183](https://github.com/writer/writer-python/issues/183)) ([b8d96bb](https://github.com/writer/writer-python/commit/b8d96bbb53442e6dc553ff7b0fa819ae8eaf4059))
* **client:** mark some request bodies as optional ([b179ebb](https://github.com/writer/writer-python/commit/b179ebbee68645ca29e21971536444b7f7f45e7f))
* **client:** only call .close() when needed ([#152](https://github.com/writer/writer-python/issues/152)) ([c999f9a](https://github.com/writer/writer-python/commit/c999f9aa55319d330102c7cf5d4d1d55843e3d6d))
* correctly handle deserialising `cls` fields ([#158](https://github.com/writer/writer-python/issues/158)) ([b05ec58](https://github.com/writer/writer-python/commit/b05ec5819968dc8874c8afbe6aeac028f334485c))
* **tests:** make test_get_platform less flaky ([#163](https://github.com/writer/writer-python/issues/163)) ([04a7500](https://github.com/writer/writer-python/commit/04a7500a29db6c430bfa4a608e894a6d7826ad00))


### Chores

* add missing isclass check ([#149](https://github.com/writer/writer-python/issues/149)) ([ceb0f57](https://github.com/writer/writer-python/commit/ceb0f57ab0ea6ea66cb193d2838f2f398ae48fe0))
* **api:** fixes to ApplicationJobs pagination ([#172](https://github.com/writer/writer-python/issues/172)) ([65f35f9](https://github.com/writer/writer-python/commit/65f35f97efe06e37e23894c78b6a016c0d1a9e07))
* **internal:** avoid pytest-asyncio deprecation warning ([#164](https://github.com/writer/writer-python/issues/164)) ([b31f771](https://github.com/writer/writer-python/commit/b31f7714fed8e35b7682801d51c76fe276ca9c16))
* **internal:** bummp ruff dependency ([#174](https://github.com/writer/writer-python/issues/174)) ([6f21ba2](https://github.com/writer/writer-python/commit/6f21ba20ab89fdcbb75a0c6b118de3534252722b))
* **internal:** bump httpx dependency ([#151](https://github.com/writer/writer-python/issues/151)) ([2bb3be6](https://github.com/writer/writer-python/commit/2bb3be6971dd94ebcc49728627c478c382db9b2f))
* **internal:** bump pyright dependency ([#161](https://github.com/writer/writer-python/issues/161)) ([062f2b0](https://github.com/writer/writer-python/commit/062f2b0389c0ae74ecd5f08f7f2927a86fb87039))
* **internal:** change default timeout to an int ([#173](https://github.com/writer/writer-python/issues/173)) ([74ed0c0](https://github.com/writer/writer-python/commit/74ed0c04b4ffa015d0ad274cde97f34d21c4595b))
* **internal:** codegen related update ([#147](https://github.com/writer/writer-python/issues/147)) ([9f6686e](https://github.com/writer/writer-python/commit/9f6686e600fdf2caad76249ed5010a7d7ecdf0e7))
* **internal:** codegen related update ([#154](https://github.com/writer/writer-python/issues/154)) ([3bb05ac](https://github.com/writer/writer-python/commit/3bb05accf88cd2bc793c418f630318d899224a07))
* **internal:** codegen related update ([#179](https://github.com/writer/writer-python/issues/179)) ([938a558](https://github.com/writer/writer-python/commit/938a558296b584de574cec7556fa419f1a15f0c3))
* **internal:** codegen related update ([#186](https://github.com/writer/writer-python/issues/186)) ([6c0e449](https://github.com/writer/writer-python/commit/6c0e4490535162c8c1fc60a96724640c51f20ba4))
* **internal:** fix devcontainers setup ([#188](https://github.com/writer/writer-python/issues/188)) ([41c98aa](https://github.com/writer/writer-python/commit/41c98aa043a31d9e64bf63726cbdfec76ee28150))
* **internal:** fix type traversing dictionary params ([#178](https://github.com/writer/writer-python/issues/178)) ([2349440](https://github.com/writer/writer-python/commit/23494409cb66956930dc6085397c6e42d8fe3321))
* **internal:** minor formatting changes ([#166](https://github.com/writer/writer-python/issues/166)) ([b4dd853](https://github.com/writer/writer-python/commit/b4dd853c159e34a85d8c79d81ab8843fa1c42893))
* **internal:** minor style changes ([#165](https://github.com/writer/writer-python/issues/165)) ([617eb51](https://github.com/writer/writer-python/commit/617eb51b94838d78068036cc37501894cbdfa938))
* **internal:** minor type handling changes ([#180](https://github.com/writer/writer-python/issues/180)) ([f625d90](https://github.com/writer/writer-python/commit/f625d90c77f97a9b926687bd6233d32ea26837c0))
* **internal:** update client tests ([#182](https://github.com/writer/writer-python/issues/182)) ([16197d5](https://github.com/writer/writer-python/commit/16197d5099440bbcc6b4d74c279c46e9a3622499))
* **internal:** update deps ([#159](https://github.com/writer/writer-python/issues/159)) ([56aa67e](https://github.com/writer/writer-python/commit/56aa67e7c3381d3dd04ece05570fbfcc026eecf7))
* **test:** update some test values ([#184](https://github.com/writer/writer-python/issues/184)) ([aafd471](https://github.com/writer/writer-python/commit/aafd47190a1029b0bdf9af0910c6e882dd6459f9))


### Documentation

* **api:** updates to API spec ([#160](https://github.com/writer/writer-python/issues/160)) ([04aa2d8](https://github.com/writer/writer-python/commit/04aa2d88053ab133038e53295b991af5098f0988))
* **api:** updates to API spec ([#168](https://github.com/writer/writer-python/issues/168)) ([66b6319](https://github.com/writer/writer-python/commit/66b63195e5d687b75be9646fec0b90dd5691a243))
* **api:** updates to API spec ([#170](https://github.com/writer/writer-python/issues/170)) ([49e58c8](https://github.com/writer/writer-python/commit/49e58c8f543a43d405a38c8346fddac4802b059f))
* **api:** updates to API spec ([#181](https://github.com/writer/writer-python/issues/181)) ([0274de8](https://github.com/writer/writer-python/commit/0274de80e13b214d17a3f241c335f0870813a36e))
* **api:** updates to API spec ([#185](https://github.com/writer/writer-python/issues/185)) ([dddde9f](https://github.com/writer/writer-python/commit/dddde9f87ce72ceb625d0579357522a476533dca))
* Fix README code samples. ([#193](https://github.com/writer/writer-python/issues/193)) ([ec22477](https://github.com/writer/writer-python/commit/ec22477ae0196da9bbb655eed38daae9986e9bfc))
* fix typos ([#153](https://github.com/writer/writer-python/issues/153)) ([5b80591](https://github.com/writer/writer-python/commit/5b805911936a8c7f0ba496d7cc092a607847ff73))
* **raw responses:** fix duplicate `the` ([#162](https://github.com/writer/writer-python/issues/162)) ([8de8d84](https://github.com/writer/writer-python/commit/8de8d8478aa54f4414a28197b4256fdb4c4d3d70))
* README code sample updates ([#189](https://github.com/writer/writer-python/issues/189)) ([1a3af86](https://github.com/writer/writer-python/commit/1a3af862cc88901ad3de8f671ad373ae0fddf52d))
* Update README. ([#192](https://github.com/writer/writer-python/issues/192)) ([6fc78a9](https://github.com/writer/writer-python/commit/6fc78a91dc079be525c3804cbece5dee5889f3dd))

## 1.6.1 (2024-12-17)

Full Changelog: [v1.6.0...v1.6.1](https://github.com/writer/writer-python/compare/v1.6.0...v1.6.1)

### Chores

* **internal:** codegen related update ([#140](https://github.com/writer/writer-python/issues/140)) ([ac0d81e](https://github.com/writer/writer-python/commit/ac0d81ec72fbdf2a9bd087645cb87cf2df2c222f))
* **internal:** fix some typos ([#145](https://github.com/writer/writer-python/issues/145)) ([cb1be53](https://github.com/writer/writer-python/commit/cb1be5358ae7ca53c9c73af6d3e2934ebdfcf1c0))

## 1.6.0 (2024-12-16)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/writer/writer-python/compare/v1.5.0...v1.6.0)

### Features

* **api:** add streaming to application generation ([#132](https://github.com/writer/writer-python/issues/132)) ([c142caa](https://github.com/writer/writer-python/commit/c142caa6b2d646b270ec50c800c37effd9b90c49))
* **api:** api update ([#131](https://github.com/writer/writer-python/issues/131)) ([efadeb6](https://github.com/writer/writer-python/commit/efadeb67a868c57775a1205a5765ccc9f45997e2))


### Chores

* **internal:** add support for TypeAliasType ([#137](https://github.com/writer/writer-python/issues/137)) ([4523c9d](https://github.com/writer/writer-python/commit/4523c9dc88771fce1b330fcf57a4499af7606c44))
* **internal:** bump pydantic dependency ([#134](https://github.com/writer/writer-python/issues/134)) ([eb1ebfe](https://github.com/writer/writer-python/commit/eb1ebfe452164409a68fc7c6d83d5fdd9ce3b089))
* **internal:** bump pyright ([#129](https://github.com/writer/writer-python/issues/129)) ([f1b2b64](https://github.com/writer/writer-python/commit/f1b2b6458b47f1861bb7d297b007b6ee09123a85))
* **internal:** bump pyright ([#136](https://github.com/writer/writer-python/issues/136)) ([66af392](https://github.com/writer/writer-python/commit/66af39233901307387129f1eb95859434ad18760))
* **internal:** updated imports ([#138](https://github.com/writer/writer-python/issues/138)) ([fc58a7d](https://github.com/writer/writer-python/commit/fc58a7de32363b013cc390ebc7c237cf74fa4137))
* make the `Omit` type public ([#133](https://github.com/writer/writer-python/issues/133)) ([94b63bb](https://github.com/writer/writer-python/commit/94b63bbc992974c0f794dcfe4ced4d7fb2284c50))


### Documentation

* **readme:** example snippet for client context manager ([#139](https://github.com/writer/writer-python/issues/139)) ([30ae872](https://github.com/writer/writer-python/commit/30ae8729b37d27572eafbd521e52eb114b635f8e))
* **readme:** fix http client proxies example ([#135](https://github.com/writer/writer-python/issues/135)) ([4e39cfe](https://github.com/writer/writer-python/commit/4e39cfec407d89fcbe03e8283e7c7bc499bc7b40))

## 1.5.0 (2024-11-28)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/writer/writer-python/compare/v1.4.0...v1.5.0)

### Features

* **api:** manual updates ([#127](https://github.com/writer/writer-python/issues/127)) ([ae6716d](https://github.com/writer/writer-python/commit/ae6716d8b2345d493ff342cb31adb02e85d7c2a8))


### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#126](https://github.com/writer/writer-python/issues/126)) ([4c04e11](https://github.com/writer/writer-python/commit/4c04e11248fac6aa0cabb94ea4abcc78252077d5))


### Chores

* fix formatting ([c33a293](https://github.com/writer/writer-python/commit/c33a2932a49d4d51ad81045ba312162f02821cbc))
* **internal:** codegen related update ([#125](https://github.com/writer/writer-python/issues/125)) ([a72d9d9](https://github.com/writer/writer-python/commit/a72d9d997ef4e0f14cfd707e143f8ca0c53c6b97))
* **internal:** fix compat model_dump method when warnings are passed ([#121](https://github.com/writer/writer-python/issues/121)) ([51a4ae5](https://github.com/writer/writer-python/commit/51a4ae539ba4cdb9b15d3a60d2ba5998a0521671))
* remove now unused `cached-property` dep ([#124](https://github.com/writer/writer-python/issues/124)) ([96715e2](https://github.com/writer/writer-python/commit/96715e244454c9b5133cae97187f61f0e6ed9b02))


### Documentation

* add info log level to readme ([#123](https://github.com/writer/writer-python/issues/123)) ([126bf74](https://github.com/writer/writer-python/commit/126bf74e40f7a69d08bef5e8d881af7efc56ae1b))

## 1.4.0 (2024-11-20)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/writer/writer-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** default timeout increase to 3 min ([#119](https://github.com/writer/writer-python/issues/119)) ([f263e59](https://github.com/writer/writer-python/commit/f263e598c17328185c43247c34fa87aca3d9a1ce))


### Chores

* rebuild project due to codegen change ([#116](https://github.com/writer/writer-python/issues/116)) ([66d114e](https://github.com/writer/writer-python/commit/66d114e2307f1e1bbcd70052a037e1ba1c5fd7d2))
* rebuild project due to codegen change ([#118](https://github.com/writer/writer-python/issues/118)) ([c527530](https://github.com/writer/writer-python/commit/c5275300b56cc724795748bfbd9811904fa2e170))

## 1.3.0 (2024-11-12)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/writer/writer-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** add streaming to kg question ([#109](https://github.com/writer/writer-python/issues/109)) ([cf85c8a](https://github.com/writer/writer-python/commit/cf85c8a2f569481605d16302a7ff785ae0225b9b))
* **api:** api update ([#108](https://github.com/writer/writer-python/issues/108)) ([785dd02](https://github.com/writer/writer-python/commit/785dd02659bd11b983bf98fc4c10923ce5dcc2a4))
* **api:** api update ([#97](https://github.com/writer/writer-python/issues/97)) ([75f6211](https://github.com/writer/writer-python/commit/75f6211064189a457b520c9dd7c7d7f9edd7d58f))
* **api:** manual updates ([#102](https://github.com/writer/writer-python/issues/102)) ([25d0319](https://github.com/writer/writer-python/commit/25d031937bab3307b96cee0682967ddbe38f78b9))
* **api:** manual updates ([#111](https://github.com/writer/writer-python/issues/111)) ([9f80bb4](https://github.com/writer/writer-python/commit/9f80bb43bf56789f53cec048102cc45611a734eb))
* **api:** manual updates ([#114](https://github.com/writer/writer-python/issues/114)) ([b9fc454](https://github.com/writer/writer-python/commit/b9fc45415b8bda5d2e0c1f8bbf2e3e064904a0b3))
* **api:** rename kg question and add text-to-graph ([#112](https://github.com/writer/writer-python/issues/112)) ([c4ac9fd](https://github.com/writer/writer-python/commit/c4ac9fd60b3d71162b179812278f6801500778c3))
* **api:** update tools api methods ([#107](https://github.com/writer/writer-python/issues/107)) ([c45ab5b](https://github.com/writer/writer-python/commit/c45ab5b4e9012cfb7118d32507b836a61fb192d6))


### Bug Fixes

* fix tool_choice schema ([403c875](https://github.com/writer/writer-python/commit/403c8755937a9c2744d0f0f214ab48fd2253180b))


### Chores

* rebuild project due to codegen change ([#100](https://github.com/writer/writer-python/issues/100)) ([fbb3664](https://github.com/writer/writer-python/commit/fbb3664b0988352f139a30fe2d10f184f4f552a6))
* rebuild project due to codegen change ([#101](https://github.com/writer/writer-python/issues/101)) ([1e0cbc1](https://github.com/writer/writer-python/commit/1e0cbc156a7f51a498f73acf006701d962ba8260))
* rebuild project due to codegen change ([#103](https://github.com/writer/writer-python/issues/103)) ([dcd2402](https://github.com/writer/writer-python/commit/dcd24028b99180a638efee77a69ed2edf43d0d1c))
* rebuild project due to codegen change ([#104](https://github.com/writer/writer-python/issues/104)) ([e9f2e66](https://github.com/writer/writer-python/commit/e9f2e66fbf9701c2c60f71f416cc2fd91182a3df))
* rebuild project due to codegen change ([#105](https://github.com/writer/writer-python/issues/105)) ([4d1c32c](https://github.com/writer/writer-python/commit/4d1c32cbe04e030d1756be2927da0a036ffe6af7))
* rebuild project due to codegen change ([#106](https://github.com/writer/writer-python/issues/106)) ([5c27b9e](https://github.com/writer/writer-python/commit/5c27b9e56736feb09c6c03790bdb0678494cff3f))
* rebuild project due to codegen change ([#113](https://github.com/writer/writer-python/issues/113)) ([477b79c](https://github.com/writer/writer-python/commit/477b79c4e0ab5edd3b4593557a01313b19148f04))
* rebuild project due to codegen change ([#99](https://github.com/writer/writer-python/issues/99)) ([490c02f](https://github.com/writer/writer-python/commit/490c02f05254023c7636cef86b6d234a81ee3d94))

## 1.2.0 (2024-10-10)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/writer/writer-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** api update ([#94](https://github.com/writer/writer-python/issues/94)) ([52fa213](https://github.com/writer/writer-python/commit/52fa213f501c771839af7753195b3ff7edea713b))

## 1.1.0 (2024-10-09)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/writer/writer-python/compare/v1.0.0...v1.1.0)

### Features

* **api:** api update ([#91](https://github.com/writer/writer-python/issues/91)) ([afcb68f](https://github.com/writer/writer-python/commit/afcb68f1e39fcba749ea302ae0d2894a37eb9909))

## 1.0.0 (2024-10-09)

Full Changelog: [v0.7.0...v1.0.0](https://github.com/writer/writer-python/compare/v0.7.0...v1.0.0)

### Features

* **api:** add model graphs.Question ([#74](https://github.com/writer/writer-python/issues/74)) ([c058228](https://github.com/writer/writer-python/commit/c058228af4d5b76fd65072476480bbd2969e1e6d))
* **api:** rename to chat_completion_chunk ([#81](https://github.com/writer/writer-python/issues/81)) ([e1fa0a5](https://github.com/writer/writer-python/commit/e1fa0a598c1b7eaf1ae2ffaee1787de3a5a87bad))
* **api:** update models in readme ([#89](https://github.com/writer/writer-python/issues/89)) ([2da514d](https://github.com/writer/writer-python/commit/2da514d83d63d0dde8b6cc4c4cf3b1b5e3ca601a))


### Bug Fixes

* change body to binary request ([9a9b656](https://github.com/writer/writer-python/commit/9a9b656757f900ea296051e9b2f637ab94bab0c2))
* **client:** avoid OverflowError with very large retry counts ([#87](https://github.com/writer/writer-python/issues/87)) ([4363005](https://github.com/writer/writer-python/commit/4363005bd134fa1e51720b22bc778eac3a6246da))
* files upload use binary request ([#85](https://github.com/writer/writer-python/issues/85)) ([105e45f](https://github.com/writer/writer-python/commit/105e45f8bbc605ee0b62e6cc0d2c8b7ab97a64bd))


### Chores

* add repr to PageInfo class ([#88](https://github.com/writer/writer-python/issues/88)) ([6110292](https://github.com/writer/writer-python/commit/611029271b81a275946781e5451733f2d811977e))
* **internal:** add support for parsing bool response content ([#84](https://github.com/writer/writer-python/issues/84)) ([1e8bc07](https://github.com/writer/writer-python/commit/1e8bc0718beee4e15f9b652a7aa2803eba16daf7))
* **internal:** codegen related update ([#76](https://github.com/writer/writer-python/issues/76)) ([d62d030](https://github.com/writer/writer-python/commit/d62d030a34cad7e7e239e936a78cb50a9dd1f57e))
* **internal:** codegen related update ([#79](https://github.com/writer/writer-python/issues/79)) ([6223c47](https://github.com/writer/writer-python/commit/6223c4776db371aa121bd0da7c773ebdb0a61f95))
* **internal:** codegen related update ([#80](https://github.com/writer/writer-python/issues/80)) ([f34c186](https://github.com/writer/writer-python/commit/f34c18645c670b36257bffd9a96077ee2d6604ea))


### Documentation

* add pagination example ([#82](https://github.com/writer/writer-python/issues/82)) ([c0c53bf](https://github.com/writer/writer-python/commit/c0c53bfd036ccf7b8dbbe0d64a2463cb73392ac2))
* **api:** updates to API spec ([#77](https://github.com/writer/writer-python/issues/77)) ([e3bd1e1](https://github.com/writer/writer-python/commit/e3bd1e13b8b10ef299c3ae24a8bda211d28bc1b2))
* **api:** updates to API spec ([#83](https://github.com/writer/writer-python/issues/83)) ([50f4e45](https://github.com/writer/writer-python/commit/50f4e4538b0ef999d8f47ca4defff50c184cb74d))
* **api:** updates to API spec ([#86](https://github.com/writer/writer-python/issues/86)) ([708f32e](https://github.com/writer/writer-python/commit/708f32e99cdeb3a9c7e5661463e1d39588e62ea6))

## 0.7.0 (2024-09-24)

Full Changelog: [v0.6.1...v0.7.0](https://github.com/writer/writer-python/compare/v0.6.1...v0.7.0)

### Features

* **api:** manual updates ([#69](https://github.com/writer/writer-python/issues/69)) ([f245fa4](https://github.com/writer/writer-python/commit/f245fa4082148f22230fd73d135276ca7202ce40))
* **api:** manual updates ([#71](https://github.com/writer/writer-python/issues/71)) ([247eef8](https://github.com/writer/writer-python/commit/247eef8d2b42f1e87284f8d50c269bad903d4e0c))
* **client:** send retry count header ([#68](https://github.com/writer/writer-python/issues/68)) ([8853d08](https://github.com/writer/writer-python/commit/8853d088a69d9f4451bf262a86b57d0af317fc56))


### Bug Fixes

* **client:** handle domains with underscores ([#67](https://github.com/writer/writer-python/issues/67)) ([73fced9](https://github.com/writer/writer-python/commit/73fced94a02d4d8cf1a93af14f577f5dba414c52))
* **lint:** format ([9ce59b1](https://github.com/writer/writer-python/commit/9ce59b1bbc7a07459c01cbc38e8a124d165b7160))


### Chores

* **internal:** codegen related update ([#65](https://github.com/writer/writer-python/issues/65)) ([8ecc8f5](https://github.com/writer/writer-python/commit/8ecc8f538ccbdb4474afedaaa58a6092c7daae38))


### Documentation

* **api:** updates to API spec ([#64](https://github.com/writer/writer-python/issues/64)) ([a86b730](https://github.com/writer/writer-python/commit/a86b730cdc19f239ac88c164d69750209b7a7df1))
* **api:** updates to API spec ([#70](https://github.com/writer/writer-python/issues/70)) ([a87a2d6](https://github.com/writer/writer-python/commit/a87a2d6cfba46d0f510fa1fcc0500dd30df2d339))

## 0.6.1 (2024-09-06)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/writer/writer-python/compare/v0.6.0...v0.6.1)

### Chores

* **internal:** codegen related update ([#60](https://github.com/writer/writer-python/issues/60)) ([861c8e5](https://github.com/writer/writer-python/commit/861c8e598b8dd280601013cbd4e28d4293d12a4a))
* pyproject.toml formatting changes ([#62](https://github.com/writer/writer-python/issues/62)) ([8839b69](https://github.com/writer/writer-python/commit/8839b699921b37f464bfa37a721cf86205355273))

## 0.6.0 (2024-08-14)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/writer/writer-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** added method to generate applications content ([#47](https://github.com/writer/writer-python/issues/47)) ([36cbfa1](https://github.com/writer/writer-python/commit/36cbfa1ea96a7d2b01d1c58ebab482d5bbdd6719))
* **api:** update via SDK Studio ([#41](https://github.com/writer/writer-python/issues/41)) ([99b6f5b](https://github.com/writer/writer-python/commit/99b6f5b881f678812a8cf68dbb4c6422f06343c0))
* **api:** update via SDK Studio ([#45](https://github.com/writer/writer-python/issues/45)) ([c5fdc23](https://github.com/writer/writer-python/commit/c5fdc23b766254505b5b11bc111ba64746da3139))
* **api:** update via SDK Studio ([#46](https://github.com/writer/writer-python/issues/46)) ([fab32ca](https://github.com/writer/writer-python/commit/fab32ca296f1f63fac0f03ae4045df61b06341d0))
* joint `upload_and_add_file_to_graph` method for graph resources ([f330ec5](https://github.com/writer/writer-python/commit/f330ec5a707d33d4355ae1f1e57e597bf9bad8ab))


### Bug Fixes

* lint (import order) ([61cf4d7](https://github.com/writer/writer-python/commit/61cf4d7f44fb7166486e2bffe06fc12bfe524119))


### Chores

* **ci:** bump prism mock server version ([#54](https://github.com/writer/writer-python/issues/54)) ([7c2f07b](https://github.com/writer/writer-python/commit/7c2f07bc8cd729e9b31b8b0eb258c2278624123b))
* fix error message import example ([#39](https://github.com/writer/writer-python/issues/39)) ([275bdd3](https://github.com/writer/writer-python/commit/275bdd379329ee5d84959fa650d62f26d93ff781))
* **internal:** add type construction helper ([#40](https://github.com/writer/writer-python/issues/40)) ([8c8b921](https://github.com/writer/writer-python/commit/8c8b921e761d96759dcf5cd531cc94ddaaae7423))
* **internal:** bump ruff version ([#50](https://github.com/writer/writer-python/issues/50)) ([4357329](https://github.com/writer/writer-python/commit/4357329088788e12fcf6a868808f708aa93897f9))
* **internal:** codegen related update ([#37](https://github.com/writer/writer-python/issues/37)) ([5427b56](https://github.com/writer/writer-python/commit/5427b5646f1f2ce8a2bab1765f21a6efe05ffcac))
* **internal:** codegen related update ([#48](https://github.com/writer/writer-python/issues/48)) ([af27fe8](https://github.com/writer/writer-python/commit/af27fe82a848f170ce800125c86acd813f452069))
* **internal:** codegen related update ([#57](https://github.com/writer/writer-python/issues/57)) ([a154150](https://github.com/writer/writer-python/commit/a1541509487aff4a5434366f1629d4729d13b692))
* **internal:** ensure package is importable in lint cmd ([#55](https://github.com/writer/writer-python/issues/55)) ([0a92c06](https://github.com/writer/writer-python/commit/0a92c067501fb9626c158caf77e133ab9102ae6f))
* **internal:** remove deprecated ruff config ([#52](https://github.com/writer/writer-python/issues/52)) ([fa82a92](https://github.com/writer/writer-python/commit/fa82a921feee401ea63cee0806c96a74826ad088))
* **internal:** test updates ([#49](https://github.com/writer/writer-python/issues/49)) ([f69e598](https://github.com/writer/writer-python/commit/f69e5980200f4e4b86b4ec76d459f1596c356396))
* **internal:** update pydantic compat helper function ([#51](https://github.com/writer/writer-python/issues/51)) ([91e721c](https://github.com/writer/writer-python/commit/91e721cf8afccae63f80659d76d1ee57a4cde228))
* **tests:** update prism version ([#38](https://github.com/writer/writer-python/issues/38)) ([c496af8](https://github.com/writer/writer-python/commit/c496af8f26608e3613f252e40c17eb2efda17c88))


### Documentation

* **api:** updates to API spec ([#53](https://github.com/writer/writer-python/issues/53)) ([df694a3](https://github.com/writer/writer-python/commit/df694a33992f622a555e708d91b2380aff0a4441))
* **api:** updates to API spec ([#58](https://github.com/writer/writer-python/issues/58)) ([f69da53](https://github.com/writer/writer-python/commit/f69da53cdede71c713ac3562eda49b87c3bd9fed))

## 0.5.0 (2024-07-14)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/writer/writer-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** codegen changes ([08baa7a](https://github.com/writer/writer-python/commit/08baa7a7826a1f613ac04659e6ff7a4962853b10))
* **api:** OpenAPI spec update via Stainless API ([#29](https://github.com/writer/writer-python/issues/29)) ([2f3b3f1](https://github.com/writer/writer-python/commit/2f3b3f1f95e56c6b98c3d9e41e1def6530388179))
* **api:** OpenAPI spec update via Stainless API ([#31](https://github.com/writer/writer-python/issues/31)) ([b59f86f](https://github.com/writer/writer-python/commit/b59f86f66dc573eb4d315bb983ac00a330d9b38c))
* **api:** OpenAPI spec update via Stainless API ([#33](https://github.com/writer/writer-python/issues/33)) ([01fa9b6](https://github.com/writer/writer-python/commit/01fa9b6fb143962d671940caa2194594d5451baf))
* **api:** update via SDK Studio ([#32](https://github.com/writer/writer-python/issues/32)) ([5dc4cba](https://github.com/writer/writer-python/commit/5dc4cba87ea0102780ff603d34c44327e2927235))

## 0.4.0 (2024-07-12)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/writer/writer-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#25](https://github.com/writer/writer-python/issues/25)) ([14d73d7](https://github.com/writer/writer-python/commit/14d73d7d933e8a8ed737e0deb94e163060e99e00))
* **api:** update via SDK Studio ([#26](https://github.com/writer/writer-python/issues/26)) ([3c48690](https://github.com/writer/writer-python/commit/3c48690799da3dfeef8b3e3f76fca7c15ebbd0d6))
* **api:** update via SDK Studio ([#27](https://github.com/writer/writer-python/issues/27)) ([773967a](https://github.com/writer/writer-python/commit/773967a17191c64e8b12dd9568cca7846a371e09))


### Bug Fixes

* **client:** correct file uploads setup ([269d7e5](https://github.com/writer/writer-python/commit/269d7e503d176832bb61eca6830d159d4b5154c4))
* **files:** remove content_length argument ([9a57374](https://github.com/writer/writer-python/commit/9a57374ed7bd8735ae11b97339ac19d5564e4038))
* **pkg:** remove unwanted files ([270fe31](https://github.com/writer/writer-python/commit/270fe3188a9dd0bba89fe3f0e69d32cc4ce77c3b))

## 0.3.0 (2024-07-12)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/writer/writer-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** update via SDK Studio ([#20](https://github.com/writer/writer-python/issues/20)) ([018271a](https://github.com/writer/writer-python/commit/018271a7c8a4a7a98937e708fe02f0b8b944df5d))

## 0.2.0 (2024-07-10)

Full Changelog: [v0.1.2...v0.2.0](https://github.com/writer/writer-python/compare/v0.1.2...v0.2.0)

### Features

* **api:** add support for graphs and files endpoints ([#15](https://github.com/writer/writer-python/issues/15)) ([173c935](https://github.com/writer/writer-python/commit/173c935d0bf8cde498e571ea4cc793994b002cc7))
* **api:** OpenAPI spec update via Stainless API ([#10](https://github.com/writer/writer-python/issues/10)) ([35aa63d](https://github.com/writer/writer-python/commit/35aa63dbd12cce5911e10671055dd1f914fbae64))
* **api:** update via SDK Studio ([#16](https://github.com/writer/writer-python/issues/16)) ([55beac6](https://github.com/writer/writer-python/commit/55beac6c92a74b2f90a5dcc10623c602d671ff03))
* **api:** update via SDK Studio ([#17](https://github.com/writer/writer-python/issues/17)) ([e098020](https://github.com/writer/writer-python/commit/e098020272202cad65f9233b238c156ca2383ec9))
* **api:** update via SDK Studio ([#18](https://github.com/writer/writer-python/issues/18)) ([ca78421](https://github.com/writer/writer-python/commit/ca78421478e6055d1147eb0bcafd88e4795c5c1f))
* Update completions_streaming.py ([764b30e](https://github.com/writer/writer-python/commit/764b30e52f6037bab4248d5f4fa2356435e2b9b2))
* Update completions_streaming.py ([00c67cc](https://github.com/writer/writer-python/commit/00c67ccacfe0d2955f00cd6f9f16a646ab2a5f22))

## 0.1.2 (2024-06-05)

Full Changelog: [v0.1.0...v0.1.2](https://github.com/writerai/writer-python/compare/v0.1.0...v0.1.2)

### Features

* **api:** update via SDK Studio ([#7](https://github.com/writerai/writer-python/issues/7)) ([84a564e](https://github.com/writerai/writer-python/commit/84a564e0c6c1acce33bd56b72caceac1a1a7e049))
* **api:** update via SDK Studio ([#8](https://github.com/writerai/writer-python/issues/8)) ([c0594c3](https://github.com/writerai/writer-python/commit/c0594c3099939bf3cd2b541ed8c87f5c68b13d79))


### Chores

* **internal:** version bump ([#5](https://github.com/writerai/writer-python/issues/5)) ([2252270](https://github.com/writerai/writer-python/commit/225227022ca403d8a60fdd7496b74c51314404e4))

## 0.1.0 (2024-06-05)

Full Changelog: [v0.1.0-alpha.3...v0.1.0](https://github.com/writerai/writer-python/compare/v0.1.0-alpha.3...v0.1.0)

### Features

* **api:** update via SDK Studio ([fe993a2](https://github.com/writerai/writer-python/commit/fe993a27d2d71e3d9f989a1900c2b413a26f6954))
* **api:** update via SDK Studio ([#10](https://github.com/writerai/writer-python/issues/10)) ([6ebe199](https://github.com/writerai/writer-python/commit/6ebe199e0b1043ed345ab6b3434d2ee116365737))
* **api:** update via SDK Studio ([#12](https://github.com/writerai/writer-python/issues/12)) ([e668e94](https://github.com/writerai/writer-python/commit/e668e9498dab939754e4dbd351f8f29ece18b622))
* **api:** update via SDK Studio ([#13](https://github.com/writerai/writer-python/issues/13)) ([aa08d76](https://github.com/writerai/writer-python/commit/aa08d76ac7a9dd0d8a40032bce986c23f8655130))
* **api:** update via SDK Studio ([#14](https://github.com/writerai/writer-python/issues/14)) ([87ce38f](https://github.com/writerai/writer-python/commit/87ce38fa40ead36136a674bfc8c330c270fb8d5e))
* **api:** update via SDK Studio ([#3](https://github.com/writerai/writer-python/issues/3)) ([3c3ae55](https://github.com/writerai/writer-python/commit/3c3ae55e3da824e8722514d589f9ccbeec62b1bb))
* **api:** update via SDK Studio ([#4](https://github.com/writerai/writer-python/issues/4)) ([2523970](https://github.com/writerai/writer-python/commit/252397069fc7012de4328fa4f874ea674d507af1))


### Chores

* go live ([#2](https://github.com/writerai/writer-python/issues/2)) ([f812fc4](https://github.com/writerai/writer-python/commit/f812fc4f9c9137907bd790477651dc8425bac0e0))

## 0.1.0-alpha.3 (2024-05-24)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/WriterColab/sdk.python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([#7](https://github.com/WriterColab/sdk.python/issues/7)) ([c65c32f](https://github.com/WriterColab/sdk.python/commit/c65c32f753a4fab19c87cc6d6a3e5fedc937460f))

## 0.1.0-alpha.2 (2024-05-16)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/WriterColab/sdk.python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#4](https://github.com/WriterColab/sdk.python/issues/4)) ([b37cf96](https://github.com/WriterColab/sdk.python/commit/b37cf9690cad490e3e7fe2ef31e9460df889dcad))

## 0.1.0-alpha.1 (2024-05-15)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/WriterColab/sdk.python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([e08da9a](https://github.com/WriterColab/sdk.python/commit/e08da9a362022809c7ce33816044f1918bca722c))
* **api:** update via SDK Studio ([44878c4](https://github.com/WriterColab/sdk.python/commit/44878c4878583052363e1d45fefd74c650ea9771))
* **api:** update via SDK Studio ([d28feb5](https://github.com/WriterColab/sdk.python/commit/d28feb5886b5a486b1caffc996f6ae7f4792aed2))
* **api:** update via SDK Studio ([f192140](https://github.com/WriterColab/sdk.python/commit/f192140264a52ac69506d51adf84e4b2b8d79104))
* **api:** update via SDK Studio ([4ac2e51](https://github.com/WriterColab/sdk.python/commit/4ac2e51ea2057da07656aa4896d11f32a580ee70))
* **api:** update via SDK Studio ([bf82bf0](https://github.com/WriterColab/sdk.python/commit/bf82bf0a1983cac58dba600ad4be45a260858055))
* **api:** update via SDK Studio ([c863077](https://github.com/WriterColab/sdk.python/commit/c863077be450adb9e0d6d17a7b24f99bbf35f267))
* **api:** update via SDK Studio ([3134c2b](https://github.com/WriterColab/sdk.python/commit/3134c2b85d35af627c61702e5e7511f03e4eadb7))
* **api:** update via SDK Studio ([c63add4](https://github.com/WriterColab/sdk.python/commit/c63add4659d4dc8ce918e09a1a347060c2f9bf38))


### Chores

* go live ([#1](https://github.com/WriterColab/sdk.python/issues/1)) ([8f24e96](https://github.com/WriterColab/sdk.python/commit/8f24e96fc0cbcef756d0774ee17047048da85fe0))
