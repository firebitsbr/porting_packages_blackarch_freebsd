PORTNAME=	dnsdiag
DISTVERSION=	v2.9.3.r0.ga76628f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	DNS Diagnostics and Performance Measurement Tools.
WWW=		https://dnsdiag.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aioquic@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-cymruwhois@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-h2@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-typing@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
