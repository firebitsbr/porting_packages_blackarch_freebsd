PORTNAME=	web2ldap
DISTVERSION=	1.8.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Full-featured LDAP client running as web application.
WWW=		https://web2ldap.de/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asn1crypto@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-iso3166@${PY_FLAVOR} \
		??/py-ldap0@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-xlwt@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
