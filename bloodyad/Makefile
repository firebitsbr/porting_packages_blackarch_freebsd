PORTNAME=	bloodyad
DISTVERSION=	283.d434b5a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An Active Directory Privilege Escalation Framework.
WWW=		https://github.com/CravateRouge/bloodyAD

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-dsinternals@${PY_FLAVOR} \
		??/py-gssapi@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-minikerberos@${PY_FLAVOR} \
		??/py-msldap@${PY_FLAVOR} \
		??/py-neo4j-driver@${PY_FLAVOR} \
		??/py-winacl@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
