PORTNAME=	typo3scan
DISTVERSION=	v1.2.final.r0.g0c4ec73
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Enumerate Typo3 version and extensions.
WWW=		https://github.com/whoot/Typo3Scan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
