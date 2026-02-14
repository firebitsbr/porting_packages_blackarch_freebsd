PORTNAME=	scanless
DISTVERSION=	90.3da40e9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Utility for using websites that can perform port scans on your behalf.
WWW=		https://github.com/vesche/scanless

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-bs4@${PY_FLAVOR} \
		??/py-crayons@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
