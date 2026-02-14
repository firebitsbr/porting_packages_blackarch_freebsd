PORTNAME=	linkedint
DISTVERSION=	1.1.FIX.r8.g89ab1d3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	LinkedIn Recon Tool.
WWW=		https://github.com/vysecurity/LinkedInt

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-thready@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
