PORTNAME=	python-ldap0
DISTVERSION=	1.4.10
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Module package for implementing LDAP clients.
WWW=		https://pypi.org/project/ldap0/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/openldap \
		??/py-pyasn1-modules@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
