PORTNAME=	python-secretsocks
DISTVERSION=	24.da5be0e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python socks server for tunneling a connection over another channel.
WWW=		https://github.com/BC-SECURITY/PySecretSOCKS

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asyncore@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
