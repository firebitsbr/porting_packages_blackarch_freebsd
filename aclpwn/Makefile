PORTNAME=	aclpwn
DISTVERSION=	4.81480cc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Active Directory ACL exploitation with BloodHound.
WWW=		https://github.com/fox-it/aclpwn.py

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-ldapdomaindump@${PY_FLAVOR} \
		??/py-neo4j-driver@${PY_FLAVOR} \
		??/py-neobolt@${PY_FLAVOR} \
		??/py-neotime@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
