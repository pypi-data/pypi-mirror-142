#!/usr/bin/env sh
#-*- coding:utf-8; mode:shell-script -*-
#
# Copyright 2020, 2021 Pradyumna Paranjape
#
# Check for network connectivity at the beginning
# This file is part of Prady_runcom.
#
# Prady_runcom is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prady_runcom is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prady_runcom.  If not, see <https://www.gnu.org/licenses/>.

# Extended for software PPSI, distributed under a slimilar (LGPLv3) license

# Variables
# IP->AP addresses

setvar () {
    usage="usage: $0 [-h] [--help] [-i IP|--ip IP] [-a AP|--ap AP] \
[-n NETCODE|--netcode NETCODE] [-r RETCODE|--retcode RETCODE]"
    help_msg="
    $usage

    DESCRIPTION: Scan current network to identify type

    Prints: ip_address ap_address netcode

    netcode:
        - 0x01: @office
        - 0x02: @home
        - 0x04: intranet connected (ping)
        - 0x08: internet (google) connected (ping)

    Optional Arguments:
    -i IP --ip IP\t\t\tIP address (hard-cast)
    -a AP --ap AP\t\t\tAP address (hard-cast)
    -n NETCODE --netcode NETCODE\tNETCODE (hard-cast)
    -r RETCODE --retcode RETCODE\tRETCODE (hard-cast)
"
    home_aps="${HOME_APS:-192.168.1.1 192.168.0.1}"
    office_aps="${OFFICE_APS:-192.168.1.101}"
    ip_addr="$(hostname -I | awk '{print $1}')"
    ap_addr="$(ip route show default \
            | grep -o "\([0-9]\{1,3\}\.\)\{3\}[0-9]\{1,3\}")"
    google_ping_cmd="ping 8.8.8.8 -c 1 -q -w 2"
    office_ping_cmd="true"
    intra_ping_cmd="ping ${ap_addr} -c 1 -q -w 2"
    inter=0
    intra=0
    home=0
    office=0
    netcode=0
    retcode=0
    for ap in ${home_aps}; do
        if [ "${ap}" = "${ap_addr}" ]; then
            home=1
            break
        fi
    done
    if [ ! ${home} ]; then
       for ap in ${office_aps}; do
           if [ "${ap}" = "${ap_addr}" ]; then
               office_ping_cmd="ping 192.168.1.101 -c 1 4 -q -w 2"
               break
           fi
       done
    fi
    unset ap
}

unset_var() {
    unset usage
    unset help_msg
    unset netcode
    unset retcode
    unset home_aps
    unset office_aps
    unset ip_addr
    unset ap_addr
    unset google_ping_cmd
    unset office_ping_cmd
    unset intra_ping_cmd
    unset inter
    unset intra
    unset office
    unset home
}

clean_exit() {
    unset_var
    if [ -n "${1}" ]; then
        exit "${1}"
    fi
    exit 0
}

cli () {
    while test $# -gt 0; do
        case "${1}" in
            -h)
                # shellcheck disable=SC2059
                printf "${usage}\n"
                exit 0
                ;;
            --help)
                # shellcheck disable=SC2059
                printf "${help_msg}\n"
                exit 0
                ;;
            -i*|--ip*)
                if [ ! "${1#*=}" = "${1}" ]; then
                    ip_addr="$(echo "${1}"| cut -d '=' -f 2)"
                else
                    shift
                    ip_addr="${1}"
                fi
                shift
                ;;
            -a*|--ap*)
                if [ ! "${1#*=}" = "${1}" ]; then
                    ap_addr="$(echo "$1"| cut -d '=' -f 2)"
                else
                    shift
                    ap_addr="${1}"
                fi
                shift
                ;;
            -n*|--netcode*)
                if [ ! "${1#*=}" = "${1}" ]; then
                    netcode="$(echo "$1"| cut -d '=' -f 2)"
                else
                    shift
                    netcode="${1}"
                fi
                shift
                ;;
            -r*|--retcode*)
                if [ ! "${1#*=}" = "${1}" ]; then
                    retcode="$(echo "$1"| cut -d '=' -f 2)"
                else
                    shift
                    retcode="${1}"
                fi
                shift
                ;;
            *)
                echo "bad argument $1" >&2
                shift
        esac
    done
}

check_ping() {
    if [ -z "${ip_addr}" ]; then
        clean_exit 1
    fi
    if $google_ping_cmd >/dev/null 2>&1 ; then
        inter=1
    fi
    if $intra_ping_cmd >/dev/null 2>&1; then
        intra=1
    fi
    if [ "${home}" -eq 0 ]; then
        if $office_ping_cmd >/dev/null 2>&1 ; then
            office=1
        fi
    fi
    if [ "${netcode}" = 0 ]; then
        netcode=$((8 * inter + 4 * intra + 2 * home + office))
    fi
}

main() {
    setvar
    cli "$@"
    check_ping
    printf "%s\t%s\t%s\n" "${ip_addr}" "${ap_addr}" "${netcode}"
    clean_exit "${retcode}"
}

main "$@"
