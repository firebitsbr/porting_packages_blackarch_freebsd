PORTNAME=	activedirectoryenum
DISTVERSION=	0.5.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Enumerate AD through LDAP.
WWW=		https://github.com/CasperGN/ActiveDirectoryEnumeration

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/bloodhound-python \
		??/impacket \
		??/py-cffi@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-ldapdomaindump@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
