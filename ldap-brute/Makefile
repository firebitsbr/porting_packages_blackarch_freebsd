PORTNAME=	ldap-brute
DISTVERSION=	21.acc06e3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A semi fast tool to bruteforce values of LDAP injections over HTTP.
WWW=		https://github.com/droope/ldap-brute

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-httmock@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
