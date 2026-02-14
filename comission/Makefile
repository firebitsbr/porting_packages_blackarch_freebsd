PORTNAME=	comission
DISTVERSION=	v1.2.0.r14.g67b890e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	WhiteBox CMS analysis.
WWW=		https://github.com/Intrinsec/comission

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-checksumdir@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-openpyxl@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
