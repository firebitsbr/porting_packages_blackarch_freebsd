PORTNAME=	hekatomb
DISTVERSION=	107.bdd53cf
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extract and decrypt all credentials from all domain computers using DPAPI.
WWW=		https://github.com/ProcessusT/HEKATOMB

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-chardet@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
