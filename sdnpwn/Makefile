PORTNAME=	sdnpwn
DISTVERSION=	85.0080574
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An SDN penetration testing toolkit.
WWW=		https://github.com/smythtech/sdnpwn

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/bridge-utils \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-openflow@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
