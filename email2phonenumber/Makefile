PORTNAME=	email2phonenumber
DISTVERSION=	29.9df9dbe
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A OSINT tool to obtain a targets phone number just by having his email address.
WWW=		https://github.com/martinvigo/email2phonenumber

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-bs4@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-soupsieve@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
