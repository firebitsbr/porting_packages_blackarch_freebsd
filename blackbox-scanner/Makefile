PORTNAME=	blackbox-scanner
DISTVERSION=	1.7a25220
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Dork scanner & bruteforcing & hash cracker with blackbox framework.
WWW=		https://github.com/sepehrdaddev/blackbox

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-passlib@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
