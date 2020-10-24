Chromium commit: `ce87fc7006cafa3938c16e6c1e97f4add509c52e`.
v8 commit: `07b0b1dcde4a99294b8028d83f4ea244885cc091`.

Arguments for building chromium (args.gn):

```
is_debug = false
symbol_level = 1
enable_linux_installer = true
```

Each URL submitted to the service will be sent to a docker container in order to be processed, each docker container runs at most 60 seconds.
Chromium browser will be run using the following command line: `chromium-browser --headless --disable-gpu --no-sandbox --js-flags=--noexpose_wasm --virtual-time-budget=60000 $(URL)`.

