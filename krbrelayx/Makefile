PORTNAME=	krbrelayx
DISTVERSION=	61.aef69a7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Kerberos unconstrained delegation abuse toolkit.
WWW=		https://github.com/dirkjanm/krbrelayx

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-impacket@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-ldapdomaindump@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
