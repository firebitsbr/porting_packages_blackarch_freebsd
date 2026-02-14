PORTNAME=	htpwdscan
DISTVERSION=	23.e995d6f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python HTTP weak pass scanner.
WWW=		https://github.com/lijiejie/htpwdScan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
