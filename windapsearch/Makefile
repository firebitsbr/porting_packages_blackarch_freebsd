PORTNAME=	windapsearch
DISTVERSION=	28.7724ec4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script to enumerate users, groups and computers from a Windows domain through LDAP queries.
WWW=		https://github.com/ropnop/windapsearch

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ldap@${PY_FLAVOR} \
		??/py-pyasn1-modules@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
