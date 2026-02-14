PORTNAME=	net-creds
DISTVERSION=	87.07a25e1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Sniffs sensitive data from interface or pcap.
WWW=		https://github.com/DanMcInerney/net-creds

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/iproute2 \
		??/net-tools \
		??/py-wsgiref@${PY_FLAVOR} \
		??/scapy \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
