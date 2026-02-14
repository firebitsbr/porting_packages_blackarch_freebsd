PORTNAME=	cisco-snmp-slap
DISTVERSION=	5.daf0589
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	IP address spoofing tool in order to bypass an ACL protecting an SNMP service on Cisco IOS devices.
WWW=		https://github.com/nccgroup/cisco-snmp-slap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
