PORTNAME=	knock
DISTVERSION=	105.9970299
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Subdomain scanner.
WWW=		https://github.com/guelfoweb/knock

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
