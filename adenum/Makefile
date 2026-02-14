PORTNAME=	adenum
DISTVERSION=	36.fbbe14d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A pentesting tool that allows to find misconfiguration through the the protocol LDAP and exploit some of those weaknesses with kerberos.
WWW=		https://github.com/SecuProject/ADenum

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ldap@${PY_FLAVOR} \
		??/py-pwntools@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
