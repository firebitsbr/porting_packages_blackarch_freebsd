PORTNAME=	bdfproxy
DISTVERSION=	107.276c367
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Patch Binaries via MITM: BackdoorFactory + mitmProxy
WWW=		https://github.com/secretsquirrel/BDFProxy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/backdoor-factory \
		??/capstone \
		??/mitmproxy \
		??/py-configobj@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
