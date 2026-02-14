PORTNAME=	breads
DISTVERSION=	131.2d97bcc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	BREaking Active Directory Security; focused on enumerating and attacking Active Directory environments through LDAP and SMB protocols.
WWW=		https://github.com/oppsec/breads

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
