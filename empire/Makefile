PORTNAME=	empire
DISTVERSION=	v6.3.0.r4.g188cbec
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A PowerShell and Python post-exploitation agent.
WWW=		https://github.com/BC-SECURITY/Empire

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/mariadb \
		lang/python \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
