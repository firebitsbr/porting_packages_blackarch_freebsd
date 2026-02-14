PORTNAME=	python-pypsrp
DISTVERSION=	0.8.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	PowerShell Remoting Protocol for Python.
WWW=		https://github.com/jborean93/pypsrp

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/krb5 \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-gssapi@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-psrpcore@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pyspnego@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
