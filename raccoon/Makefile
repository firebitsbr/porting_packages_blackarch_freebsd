PORTNAME=	raccoon
DISTVERSION=	190.44024ab
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A high performance offensive security tool for reconnaissance and vulnerability scanning.
WWW=		https://github.com/evyatarmeged/Raccoon

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-xmltodict@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
