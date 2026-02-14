PORTNAME=	python2-pip
DISTVERSION=	20.3.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The PyPA recommended tool for installing Python packages.
WWW=		https://pip.pypa.io/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/${_deps[@]/#/python2-} \
		??/py-ipaddress@${PY_FLAVOR}



USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
