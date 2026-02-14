PORTNAME=	python2-ldapdomaindump
DISTVERSION=	0.9.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Active Directory information dumper via LDAP.
WWW=		https://pypi.org/project/ldapdomaindump/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
