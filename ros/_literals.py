from typing import Literal, Union

AnyLiteral = Literal["any"]
IPProtocol = (
    Literal[
        "dccp",
        "ddp",
        "egp",
        "encap",
        "etherip",
        "ggp",
        "gre",
        "hmp",
        "icmp",
        "icmpv6",
        "idpr-cmtp",
        "igmp",
        "ipencap",
        "ipip",
        "ipsec-ah",
        "ipsec-esp",
        "ipv6-encap",
        "ipv6-frag",
        "ipv6-nonxt",
        "ipv6-opts",
        "ipv6-route",
        "iso-tp4",
        "l2tp",
        "ospf",
        "pim",
        "pup",
        "rdp",
        "rspf",
        "rsvp",
        "sctp",
        "st",
        "tcp",
        "udp",
        "udp-lite",
        "vmtp",
        "vrrp",
        "xns-idp",
        "xtp",
    ],
)

MACProtocol = Literal[
    "acap",
    "activision",
    "afpovertcp",
    "agentx",
    "any",
    "aol",
    "apple-licman",
    "appleqtc",
    "appleqtcsrvr",
    "appleugcontrol",
    "arcp",
    "asia",
    "asip-webadmin",
    "asipregistry",
    "aurp",
    "auth",
    "avt-profile-1",
    "avt-profile-2",
    "bdp",
    "bftp",
    "bgp",
    "biff",
    "bootpc",
    "bootps",
    "btserv",
    "buddyphone",
    "ccmail",
    "cfdptkt",
    "chargen",
    "cops",
    "cpq-wbem",
    "csnet-ns",
    "daytime",
    "dict",
    "discard",
    "discovery",
    "distributed-net",
    "dixie",
    "dlsrap",
    "dlsrpn",
    "dlswpn",
    "dns",
    "dns2go",
    "doom",
    "dsp",
    "dtspcd",
    "echo",
    "epmap",
    "eppc",
    "esro-emsdp",
    "esro-gen",
    "etftp",
    "fcp-addr-srvr1",
    "fcp-addr-srvr2",
    "fcp-cics-gw1",
    "fcp-srvr-inst1",
    "fcp-srvr-inst2",
    "finger",
    "ftp",
    "ftp-data",
    "glimpse",
    "gopher",
    "h323gatestat",
    "h323hostcall",
    "half-life",
    "hbci",
    "hostname",
    "hotsync-1",
    "hotsync-2",
    "hsrp",
    "htcp",
    "http",
    "http-alt",
    "https",
    "ica",
    "icabrowser",
    "icpv2",
    "icq",
    "imail-www",
    "imap3",
    "imaps",
    "ipp",
    "irc",
    "ircu",
    "isakmp",
    "iso-tsap",
    "kerberos",
    "klogin",
    "l2tp",
    "ldap",
    "ldaps",
    "link",
    "linuxconf",
    "liquidaudio",
    "lotusnote",
    "lpr",
    "mac-srvr-admin",
    "madcap",
    "matip-type-a",
    "matip-type-b",
    "mc-ftp",
    "mgcp-callagent",
    "mgcp-gateway",
    "microcom-sbp",
    "mobileip",
    "mountd",
    "mpp",
    "ms-rpc",
    "ms-sql-m",
    "ms-sql-s",
    "ms-streaming",
    "ms-wbt-server",
    "msbd",
    "msg-auth",
    "msg-icp",
    "msql",
    "mtp",
    "mysql",
    "mzap",
    "name",
    "napster",
    "napster-2",
    "napster-3",
    "net-assistant",
    "netbios-dgm",
    "netbios-ns",
    "netbios-ssn",
    "netrek",
    "netstat",
    "nextstep",
    "nfile",
    "nfs",
    "nicname",
    "nntp",
    "nntps",
    "ntp",
    "odette-ftp",
    "odmr",
    "oracle-sql",
    "pcanywheredata",
    "pcanywherestat",
    "pdap-np",
    "pgp5-key",
    "photuris",
    "pop2",
    "pop3",
    "pop3s",
    "poppassd",
    "pptp",
    "prospero-np",
    "pwdgen",
    "qotd",
    "quake",
    "quake-world",
    "quake3",
    "radius",
    "radius-acct",
    "rap",
    "re-mail-ck",
    "realsecure",
    "reftek",
    "rip",
    "ripng",
    "rje",
    "rlogin",
    "rlp",
    "rrp",
    "rsvp-tunnel",
    "rtp",
    "rtsp",
    "rwhois",
    "rwp",
    "secureid",
    "sftp",
    "sgmp",
    "sift-uft",
    "sip",
    "slmail",
    "smb",
    "smtp",
    "smux",
    "snmp",
    "snpp",
    "socks",
    "sql*net",
    "sql-net",
    "squid",
    "ssh",
    "statsrv",
    "sunrpc",
    "supdup",
    "swat",
    "syslog",
    "systat",
    "t.120",
    "tacacs",
    "talk",
    "tcp-id-port",
    "tcpmux",
    "telnet",
    "tftp",
    "tftp-mcast",
    "timbuktu",
    "timbuktu-srv1",
    "timbuktu-srv2",
    "timbuktu-srv3",
    "timbuktu-srv4",
    "time",
    "tinc",
    "tlisrv",
    "uls",
    "unreal",
    "uucp-path",
    "vemmi",
    "veracity",
    "virtualuser",
    "vmnet",
    "vnc-1",
    "vnc-2",
    "webobjects",
    "whois++",
    "winbox",
    "winbox-old",
    "winbox-old-tls",
    "wingate",
    "wlbs",
    "x11",
    "xdmcp",
    "yahoo",
    "z39.50",
]

PortLiteral = Literal[
    "acap",
    "activision",
    "afpovertcp",
    "agentx",
    "aol",
    "apple-licman",
    "appleqtc",
    "appleqtcsrvr",
    "appleugcontrol",
    "arcp",
    "asia",
    "asip-webadmin",
    "asipregistry",
    "aurp",
    "auth",
    "avt-profile-1",
    "avt-profile-2",
    "bdp",
    "bftp",
    "bgp",
    "biff",
    "bootpc",
    "bootps",
    "btserv",
    "buddyphone",
    "ccmail",
    "cfdptkt",
    "chargen",
    "cops",
    "cpq-wbem",
    "csnet-ns",
    "daytime",
    "dict",
    "discard",
    "discovery",
    "distributed-net",
    "dixie",
    "dlsrap",
    "dlsrpn",
    "dlswpn",
    "dns",
    "dns2go",
    "doom",
    "dsp",
    "dtspcd",
    "echo",
    "epmap",
    "eppc",
    "esro-emsdp",
    "esro-gen",
    "etftp",
    "fcp-addr-srvr1",
    "fcp-addr-srvr2",
    "fcp-cics-gw1",
    "fcp-srvr-inst1",
    "fcp-srvr-inst2",
    "finger",
    "ftp",
    "ftp-data",
    "glimpse",
    "gopher",
    "h323gatestat",
    "h323hostcall",
    "half-life",
    "hbci",
    "hostname",
    "hotsync-1",
    "hotsync-2",
    "hsrp",
    "htcp",
    "http",
    "http-alt",
    "https",
    "ica",
    "icabrowser",
    "icpv2",
    "icq",
    "imail-www",
    "imap3",
    "imaps",
    "ipp",
    "irc",
    "ircu",
    "isakmp",
    "iso-tsap",
    "kerberos",
    "klogin",
    "l2tp",
    "ldap",
    "ldaps",
    "link",
    "linuxconf",
    "liquidaudio",
    "lotusnote",
    "lpr",
    "mac-srvr-admin",
    "madcap",
    "matip-type-a",
    "matip-type-b",
    "mc-ftp",
    "mgcp-callagent",
    "mgcp-gateway",
    "microcom-sbp",
    "mobileip",
    "mountd",
    "mpp",
    "ms-rpc",
    "ms-sql-m",
    "ms-sql-s",
    "ms-streaming",
    "ms-wbt-server",
    "msbd",
    "msg-auth",
    "msg-icp",
    "msql",
    "mtp",
    "mysql",
    "mzap",
    "name",
    "napster",
    "napster-2",
    "napster-3",
    "net-assistant",
    "netbios-dgm",
    "netbios-ns",
    "netbios-ssn",
    "netrek",
    "netstat",
    "nextstep",
    "nfile",
    "nfs",
    "nicname",
    "nntp",
    "nntps",
    "ntp",
    "odette-ftp",
    "odmr",
    "oracle-sql",
    "pcanywheredata",
    "pcanywherestat",
    "pdap-np",
    "pgp5-key",
    "photuris",
    "pop2",
    "pop3",
    "pop3s",
    "poppassd",
    "pptp",
    "prospero-np",
    "pwdgen",
    "qotd",
    "quake",
    "quake-world",
    "quake3",
    "radius",
    "radius-acct",
    "rap",
    "re-mail-ck",
    "realsecure",
    "reftek",
    "rip",
    "ripng",
    "rje",
    "rlogin",
    "rlp",
    "rrp",
    "rsvp-tunnel",
    "rtp",
    "rtsp",
    "rwhois",
    "rwp",
    "secureid",
    "sftp",
    "sgmp",
    "sift-uft",
    "sip",
    "slmail",
    "smb",
    "smtp",
    "smux",
    "snmp",
    "snpp",
    "socks",
    "sql*net",
    "sql-net",
    "squid",
    "ssh",
    "statsrv",
    "sunrpc",
    "supdup",
    "swat",
    "syslog",
    "systat",
    "t.120",
    "tacacs",
    "talk",
    "tcp-id-port",
    "tcpmux",
    "telnet",
    "tftp",
    "tftp-mcast",
    "timbuktu",
    "timbuktu-srv1",
    "timbuktu-srv2",
    "timbuktu-srv3",
    "timbuktu-srv4",
    "time",
    "tinc",
    "tlisrv",
    "uls",
    "unreal",
    "uucp-path",
    "vemmi",
    "veracity",
    "virtualuser",
    "vmnet",
    "vnc-1",
    "vnc-2",
    "webobjects",
    "whois++",
    "winbox",
    "winbox-old",
    "winbox-old-tls",
    "wingate",
    "wlbs",
    "x11",
    "xdmcp",
    "yahoo",
    "z39.50",
]
