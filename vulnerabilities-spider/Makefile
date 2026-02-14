PORTNAME=	vulnerabilities-spider
DISTVERSION=	1.426e70f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool to scan for web vulnerabilities.
WWW=		https://github.com/muhammad-bouabid/Vulnerabilities-spider

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/gtk3 \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-gobject@${PY_FLAVOR} \
		??/py-pymysql@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/pygtk \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
