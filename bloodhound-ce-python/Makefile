PORTNAME=	bloodhound-ce-python
DISTVERSION=	v1.0.1.r211.g6fa5ba5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python data collector for Bloodhound community edition (v5)
WWW=		https://github.com/dirkjanm/BloodHound.py

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
