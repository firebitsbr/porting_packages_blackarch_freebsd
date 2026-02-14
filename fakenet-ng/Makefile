PORTNAME=	fakenet-ng
DISTVERSION=	315.3b7aea2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Next Generation Dynamic Network Analysis Tool.
WWW=		https://github.com/fireeye/flare-fakenet-ng

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dnslib@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-netfilterqueue@${PY_FLAVOR} \
		??/py-pydivert@${PY_FLAVOR} \
		??/py-pyftpdlib@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-win_inet_pton@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
