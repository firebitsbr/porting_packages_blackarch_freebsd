PORTNAME=	python-ldaptor
DISTVERSION=	21.2.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Pure-Python Twisted library for LDAP.
WWW=		https://pypi.org/project/ldaptor/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-passlib@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		??/py-zope-interface@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
