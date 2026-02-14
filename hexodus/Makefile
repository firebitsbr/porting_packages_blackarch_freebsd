PORTNAME=	hexodus
DISTVERSION=	72.69a96f6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python framework project designed to enumerate and help in Active Directory attacks through Windows protocols like SMB, LDAP, WinRM and other.
WWW=		https://github.com/0xdsm/hexodus

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-flask@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
