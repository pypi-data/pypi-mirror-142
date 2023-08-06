# Rialtic insight engine schema in Python

This repo contains translation of InsightEngine Request/Response schema to Python.
It uses `fhir.resources` internally (see https://pypi.org/project/fhir.resources/).

## Release to Nexus

A GitHub workflow called `do_release_nexus` is also provided for this task. 

On a local machine, you can do:

1. Merge the `develop` branch into master
2. Set environment variables

```shell
export NEXUS_USERNAME=...
export NEXUS_PASSWORD=...
export RIALTIC_PRE_RELEASE=1
export NEXUS_LIBRARIES_PRE_RELEASE_UPSTREAM=https://artifacts.services.rialtic.dev/repository/internal-snapshot-python/
export NEXUS_LIBRARIES_UPSTREAM=https://artifacts.services.rialtic.dev/repository/libraries-python/
export NEXUS_DOWNSTREAM=https://artifacts.services.rialtic.dev/repository/libraries-group-python/simple/
```

3. Make sure you have configured the Nexus repositories in `poetry`:

```shell
poetry config repositories.nexus_libraries_upstream ${NEXUS_LIBRARIES_UPSTREAM}
poetry config repositories.nexus_libraries_pre_release_upstream ${NEXUS_LIBRARIES_PRE_RELEASE_UPSTREAM}
poetry config repositories.nexus_downstream ${NEXUS_DOWNSTREAM}
poetry config http-basic.nexus_downstream ${NEXUS_USERNAME} ${NEXUS_PASSWORD}
```

(This step only needs to be done once for all repositories.)

4. If you want to do a pre-release first, then run `make release`, 
   and it will release to repository `internal-snapshot-python` instead of `libraries-python`.
5. Otherwise, run `RIALTIC_PRE_RELEASE=0 make release`
