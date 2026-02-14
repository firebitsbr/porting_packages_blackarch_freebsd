PORTNAME=	jeopardize
DISTVERSION=	5.34f1d07
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A low(zero) cost threat intelligence & response tool against phishing domains.
WWW=		https://github.com/utkusen/jeopardize

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
