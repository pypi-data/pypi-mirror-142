#!/usr/bin/env bash
#
# fio.sh - Wrapper for the Flexible I/O tester
#
# Functions:
#
# fio.env              - Setup default environment variables and check required ones
# fio.run              - Translate ENV. VARS. into FIO_ARGS and run fio
#
## Variables EXPORTED by module:
#
# FIO_BIN               - Absolute PATH to fio binary (DEFAULT - see code)
#
# Variables EXPORTED by fio.run:
#
# FIO_ARGS              - Complete set of arguments for fio command
#
fio.env() {
  if [[ ! -v FIO_FILENAME ]]; then
    cij.err "fio.env: FIO_FILENAME must be set"
    return 1
  fi

  FIO_BIN=${FIO_BIN:=/usr/local/bin/fio}; export FIO_BIN
  FIO_ARGS=${FIO_ARGS:=}; export FIO_ARGS

  return 0
}

fio.run() {
  if ! fio.env; then
    cij.err "fio.env failed"
    return 1
  fi

  local _args="${FIO_ARGS}"

  cij.cmd "${FIO_BIN} ${_args}"
  return $?
}

