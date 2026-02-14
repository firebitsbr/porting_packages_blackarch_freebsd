PORTNAME=	scanqli
DISTVERSION=	26.40a028d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	SQLi scanner to detect SQL vulns.
WWW=		https://github.com/bambish/ScanQLi

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-optparse-pretty@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-validators@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
