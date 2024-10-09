# Changelog

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
