#!/bin/bash
#
# Run io_uring smoke tests - 01
#
# shellcheck disable=SC2119
#
CIJ_TEST_NAME=$(basename "${BASH_SOURCE[0]}")
export CIJ_TEST_NAME
# shellcheck source=modules/cijoe.sh
source "$CIJ_ROOT/modules/cijoe.sh"
test::enter

: "${FIO_FILENAME?Must be set and non-empty}"

# Run actual test - Basic sequential + verify workload
#FIO_FILENAME="${FIO_FILENAME}"
FIO_IOENGINE="io_uring"
FIO_BLOCKSIZE="256k"
FIO_IODEPTH="1"
FIO_SIZE="2G"
FIO_READWRITE="write"

main() {
  _name="FIO"
  _name="${_name}_EN-${FIO_IOENGINE}"
  _name="${_name}_BS-${FIO_BLOCKSIZE}"
  _name="${_name}_QD-${FIO_IODEPTH}"
  _name="${_name}_SZ-${FIO_SIZE}"
  _name="${_name}_RT-NA"
  _name="${_name}_RW-${FIO_READWRITE}"
  _name="${_name}_RZ-NA"

#  FIO_DOLOGS=1
#  FIO_DOLOGS_ROOT="/tmp/${_name}_${CIJ_TEST_ARB}_"

  FIO_ARGS=""
  FIO_ARGS="${FIO_ARGS} --bs=${FIO_BLOCKSIZE}"
  FIO_ARGS="${FIO_ARGS} --iodepth=${FIO_IODEPTH}"
  FIO_ARGS="${FIO_ARGS} --size=${FIO_SIZE}"
  FIO_ARGS="${FIO_ARGS} --readwrite=${FIO_READWRITE}"
  FIO_ARGS="${FIO_ARGS} --direct=1"
  FIO_ARGS="${FIO_ARGS} --do_verify=1"
  FIO_ARGS="${FIO_ARGS} --verify=crc32c-intel"
  FIO_ARGS="${FIO_ARGS} --verify_fatal=1"
  FIO_ARGS="${FIO_ARGS} --ioengine=${FIO_IOENGINE}"
  FIO_ARGS="${FIO_ARGS} --filename=${FIO_FILENAME}"
  FIO_ARGS="${FIO_ARGS} --name=_${_name}"

  cij.info "Running '$_name'"
  if ! fio.run; then
    test.fail
  fi

  test.pass
}

main
